import pandas
import Levenshtein as l
from sqlalchemy import create_engine
import urllib
import numpy as np


SQL_customers = """select *
from
dbo.OXB_Customer"""

SQL_billingaddresses="""select '' as billingid, '' as custid, c.BillAddressAddr1 as billto,
c.BillAddressAddr2 as billingaddress1,c.BillAddressAddr3 as billingaddress2,
c.BillAddressCity, c.BillAddressState as billingaddstate, c.BillAddressPostalCode as billingaddzip,
c.Phone as billingphone, '' as billingphoneextn,c.Email as billingemail, '' as billingnote,
'' as oldbillingid
from dbo.OXB_Customer c"""

SQL_invoice_orders="""select '' as orderid, rj.custid, rj.billingid, rj.jobsiteid,oxi.ShipDate as orderdate, 
oxil.Memo as ordercomments, '' as orderadd, oxil.SubTotal as orderamount, oxi.TxnID
from AcquisitionTools.dbo.RAWjobsites rj
inner join
OXB_Invoice oxi
on oxi.CustomerRefListID=rj.oldjobsiteid
left join
OXB_InvoiceLine oxil
on oxil.TxnID=oxi.TxnID"""

SQL_invoice_order_details="""select distinct '' as orderdetailid, ro.orderid,olm. WindRiverID as orderserviceid , olm.[Wind River Item] as orderservicedescription, 
il.InvoiceLineQuantity as orderservicequantity, il.InvoiceLineAmount,
il.InvoiceLineRate as orderserviceprice, olm.ListID,ro.orderponumber
from AcquisitionTools.dbo.RAWorders ro
inner join
OXB_InvoiceLine il
on ro.orderponumber=il.TxnID
inner join
OXB_LINEMAPPING olm
on olm.ListID=il.InvoiceLineItemRefListID"""


SQL_interactions = """select '' as interactionid, '' as custid, '' as jobsitedid, '' as orderId,
'' as interactiondate, 'CSC - Note' as interactiontype, ca.Notes as interationnote,
1 as status, '' as reminderdate, getdate() as createddate, getdate() as updateddate 
from dbo.OXB_CustomerAddtionalNote ca"""


params_tools = urllib.parse.quote("DRIVER=ODBC Driver 13 for SQL Server;SERVER=WRE-SASAC;DATABASE=AcquisitionTools;trusted_connection=yes;")
engine_tools = create_engine('mssql+pyodbc:///?odbc_connect=%s' % params_tools)
with engine_tools.connect() as cn_tools:
    
    RAWcustomers = pandas.read_sql_table('RAWcustomers', cn_tools)
    RAWbillingaddress = pandas.read_sql_table('RAWbillingaddress', cn_tools)
    RAWjobsites = pandas.read_sql_table('RAWjobsites', cn_tools)
    
    RAWorders = pandas.read_sql_table('RAWorders', cn_tools)
    RAWorderdetails = pandas.read_sql_table('RAWorderdetails', cn_tools)
    RAWinteractions = pandas.read_sql_table('RAWinteractions', cn_tools)
    # load the source tables
    params_sandbox = urllib.parse.quote("DRIVER=ODBC Driver 13 for SQL Server;SERVER=WRE-SASAC;DATABASE=AcquisitionSandbox;trusted_connection=yes;")
    engine_sandbox = create_engine('mssql+pyodbc:///?odbc_connect=%s' % params_sandbox)
    with engine_sandbox.connect() as cn_sandbox:

        
        #invoice_lines = pandas.read_sql(sql=SQL_invoice_line, con=cn_sandbox)
        #existing_jobsites = pandas.read_sql(sql=SQL_existing_cust_jobsites, con=cn_sandbox)
        #existing_interactions=pandas.read_sql(sql=SQL_existing_interactions, con=cn_sandbox)
        #new_invoices = pandas.read_sql(sql=SQL_invoices_new_customers, con=cn_sandbox)
        #customers = pandas.read_sql(sql=SQL_customers, con=cn_sandbox)
        #billingaddresses=pandas.read_sql(sql=SQL_billingaddresses, con=cn_sandbox)
        #RAWorders = pandas.DataFrame(index = np.arange(0, invoices.shape[0]) + np.arange(0, new_invoices.shape[0]), columns = list(RAWorders))
        invoices = pandas.read_sql(sql=SQL_invoice_orders, con=cn_sandbox)
        invoice_lines=pandas.read_sql(sql=SQL_invoice_order_details,con=cn_sandbox)
        #RAWorderdetails = pandas.DataFrame(index = np.arange(0, invoice_lines.shape[0]), columns = list(RAWorderdetails))
        #RAWinteractions = pandas.DataFrame(index = np.arange(0,existing_interactions.shape[0]), columns=list(RAWinteractions))
        # Drummac orderid = 9000003
        #orderid=2000862
        # Drummac serviceid=15371944
        #orderserviceid = 19224018
        
        #custid = 0
        #billingid=0
        #jobsiteid = 0

        #RAWcustomers = pandas.DataFrame(index = np.arange(0, customers.shape[0]), columns = list(RAWcustomers))

        #Rawbillingaddress=pandas.DataFrame(index = np.arange(0, billingaddresses.shape[0]), columns = list(RAWbillingaddress))
        RAWbillingaddress=pandas.DataFrame(index = np.arange(0, billingaddresses.shape[0]), columns = list(RAWbillingaddress))    
        RAWjobsites=pandas.DataFrame(index = np.arange(0, customers.shape[0]), columns = list(RAWjobsites))
        RAWorders=pandas.DataFrame(index = np.arange(0, invoices.shape[0]), columns = list(RAWorders))
        RAWorderdetails=pandas.DataFrame(index=np.arange(0, invoice_lines.shape[0]), columns=list(RAWorderdetails))


        commercialWords=[
            '& sons',
            '& Sons',
            '& sons',
            '& Sons',
            '& Hardware,'
            '& hardware'
            '& Recreation',
            '& recreation',
            'aviation',
            'Aviation',
            'apartment',
            'Apartment',
            'associate',
            'Associate',
            'Assisted living,'
            'assisted living',
            'Association',
            'association',
            'Bagel',
            'Bar',
            'bar',
            'bagel',
            'Brewery'
            'brewery'
            'Build',
            'build',
            'build',
            'Com' ,
            'Com',
            'com',
            'Company',
            'company',
            'Coffee',
            'coffee',
            'Coffee',
            'church',
            'Church',
            'contractor',
            'Contractor',
            'construction',
            'Construction',
            'condominium',
            'Condominium',
            'Co, Inc',
            'co, inc',
            'co,inc',
            'Concrete',
            'concrete',
            'Drive',
            'drive',
            'District',
            'district',
            'Development',
            'development',
            'Equipment',
            'equipment',
            'Excavation',
            'excavation',
            'England',
            'england',
            'Estates',
            'estates',
            'Enterprise',
            'enterprise',
            'Family',
            'family',
            'Facility',
            'facility',
            'Hotel',
            'hotel',
            'Heat',
            'heat',
            'Inn',
            'inn',
            'Investor',
            'Investment'
            'investor',
            'Inc',
            'Inc',
            'inc',
            'llc',
            'LLC',
            'management',
            'Management',
            'mgmt',
            'Motel',
            'motel',
            'Operating',
            'operating',
            'Office',
            'office',
            'office',
            'Park',
            'park',
            'Parks',
            'parks',
            'Paint',
            'paint',
            'Property',
            'property',
            'plumbing' ,
            'Plumbing' ,
            'Pizza',
            'pizza',
            'Recreation',
            'recreation',
            'Restaurant',
            'restaurant',
            'realty',
            'realty',
            'rectory',
            'Rectory',
            'Rectory',
            'school',
            'School',
            'service',
            'Service',
            'septic',
            'Septic',
            'Store',
            'store',
            'Trade',
            'trade',
            'Tech',
            'tech',
            'Town',
            'town',
            'Water',
            'water',
            'Inc.',
            'inc.',
            'express',
            'Express']



        def convertCommercial(string):

            return any(substring in string for substring in commercialWords)

        def get_phone(phone):
            if phone is not None and phone[:1] != '1':
                return ri.Phone.replace('-','')[:10]
            elif phone is not None:
                return ri.Phone.replace('-','')[1:9]
            elif phone is None:
                return None
            else:
                return phone

        def GetTermId(argument):
            switcher = {
                "Net 15":6,
                "Net 30":2,
                "Net 30/":2,
                "Net 30(Per Jules)":2,
                "Net 60":7,
                "Net 10":5
            }
            #print(switcher.get(argument,1))
            return switcher.get(argument,1)



        #.to_clipboard(sep = '\t', index = False)
        """for i, ri in customers.iterrows():
            print('i' , i, custid)
            custid = custid + 1
            RAWcustomers.custid[i] = custid
            #RAWcustomers.custacquisitionid[i] = 106
            RAWcustomers.custacquisitionid=113
            RAWcustomers.custaddcity[i] = ri.BillAddressCity
            RAWcustomers.custaddress1[i] = ri.BillAddressAddr2
            RAWcustomers.custaddress2[i] = ri.BillAddressAddr3
            RAWcustomers.custaddstate[i] = ri.BillAddressState
            RAWcustomers.custaddzip[i] = ri.BillAddressPostalCode[:5] if ri.BillAddressPostalCode is not None else str(ri.BillAddressPostalCode)
            try:
                RAWcustomers.custlastname[i] = ri.BillAddressAddr1 if (convertCommercial(ri.BillAddressAddr1)) is True else ri.LastName
            except TypeError:
                print('Dont know what is going on')
            #RAWcustomers.custlastname[i]=ri.LastName
            try:
                RAWcustomers.custfirstname[i] = None if (convertCommercial(ri.BillAddressAddr1)) is True else ri.FirstName
            except TypeError:
                print('Dont know what is going on')
            try:
                RAWcustomers.custcategoryid[i] = 2 if (convertCommercial(ri.BillAddressAddr1)) is True else 1
            except TypeError:
                print('Dont know what is going on')
            try:
                RAWcustomers.custprimaryphone[i] = get_phone(ri.Phone)
            except AttributeError:
                print('Dont know what is going on')
            #RAWcustomers.custprimaryphone[i] = ri.Phone
            RAWcustomers.custprimaryphoneext[i] = ri.Phone[-3:] if ri.Phone is not None and 'ext' in ri.Phone else None
            try:
                RAWcustomers.custsecondaryphone[i] = get_phone(ri.AltPhone)
            except AttributeError:
                print('Dont know what is going on')
            RAWcustomers.custemail[i]=ri.Email
            try:
                RAWcustomers.custfax[i]=get_phone(ri.Fax)
            except AttributeError:
                print('Dont know what is going on')
            RAWcustomers.custshowprice[i] = True
            RAWcustomers.custisCOD[i]=1 if ri.TermsRefFullName=="Due on receipt" else 0
            RAWcustomers.custinvtermid[i] = GetTermId(ri.TermsRefFullName)
            RAWcustomers.custcreditlimit= None
            RAWcustomers.oldcustid[i] = ri.ListID"""

        print(RAWcustomers.shape)
        print(RAWbillingaddress.shape)
        print(RAWorders.shape)
        print(RAWorderdetails.shape)
        
        #orderid=1
        #for i, ri in invoices.iterrows():
            

            #orderid = orderid + 1
            #print('i' , i, ri['custid'])
            #RAWorders['orderid'][i] = "OXB" + str(orderid).zfill(7)

            #RAWorders['orderdate'][i] = ri['ShipDate']
            #RAWorders['orderdate'][i]=ri['orderdate']
            #RAWorders['orderamount'][i] = ri['orderamount']
            #RAWorders['orderponumber'][i] = ri['TxnID']  
            #RAWorders['jobsiteid'][i] = ri['jobsiteid']
            #RAWorders['custid'][i] = ri['custid']
            #RAWorders['ordercomments']=ri['ordercomments']
            #RAWorders['billingid']=ri['billingid']

        orderdetailid=0

        for i, ri in invoice_lines.iterrows():
            print ('i', i, orderdetailid)
            orderdetailid = orderdetailid + 1
            RAWorderdetails.orderdetailid[i] = orderdetailid
            #RAWorderdetails.orderid[k] = "A1G" + str(orderid).zfill(7)
            RAWorderdetails.orderid=ri['orderid']
            RAWorderdetails.orderserviceid[i] = ri['orderserviceid']
            RAWorderdetails.orderservicedescription[i] = ri['orderservicedescription']
            RAWorderdetails.orderservicequantity[i]= ri['orderservicequantity']
            RAWorderdetails.orderserviceprice[i] = ri['orderserviceprice']
            RAWorderdetails.orderservicerevenue[i] = ri['InvoiceLineAmount']


            