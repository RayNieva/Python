RAWorders.to_clipboard(sep = '\t', index = False)
RAWorderdetails.to_clipboard(sep = '\t', index = False)


;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

import pandas
import Levenshtein as l
from sqlalchemy import create_engine
import urllib
import numpy as np



SQL_invoices = """select
i.TxnID, i.RefNumber, I.ShipDate, I.Subtotal, i.CustomerRefListID, 
i.ShipAddressAddr2,i.ShipAddressAddr3,i.ShipAddressAddr4,
c.ShipAddressAddr1 'custaddr1', c.ShipAddressAddr2 'custaddr2', 
c.ShipAddressAddr3 'custaddr3', c.ShipAddressAddr4 'custaddr4'
from
dbo.A1_2_Invoice i left join
dbo.A1_Invoice i2 on i2.TxnID = i.TxnID inner join
dbo.A1_2_Customer c on c.ListID = i.CustomerRefListID
where
i2.TxnID is null"""

"""
def sql_invoices(table1,table2):
    
    select
    i.TxnID, i.RefNumber, I.ShipDate, I.Subtotal, i.CustomerRefListID, 
    i.ShipAddressAddr2,i.ShipAddressAddr3,i.ShipAddressAddr4,
    c.ShipAddressAddr1 'custaddr1', c.ShipAddressAddr2 'custaddr2', 
    c.ShipAddressAddr3 'custaddr3', c.ShipAddressAddr4 'custaddr4'
    from
    dbo.table1_Invoice i left join
    dbo.table2_Invoice i2 on i2.TxnID = i.TxnID inner join
    dbo.table1_Customer c on c.ListID = i.CustomerRefListID
    where
    i2.TxnID is null
    
    
    #table1='Drummac'
    SQL_invoicesQ="select i.TxnID, i.RefNumber, I.ShipDate, I.Subtotal, i.CustomerRefListID,\n"
    SQL_invoicesQ=SQL_invoicesQ + "i.ShipAddressAddr2,i.ShipAddressAddr3,i.ShipAddressAddr4,\n"
    SQL_invoicesQ=SQL_invoicesQ + "c.ShipAddressAddr1 'custaddr1', c.ShipAddressAddr2 'custaddr2',\n" 
    SQL_invoicesQ=SQL_invoicesQ + "c.ShipAddressAddr3 'custaddr3', c.ShipAddressAddr4 'custaddr4'\n"
    SQL_invoicesQ=SQL_invoicesQ + "from\n"
    SQL_invoicesQ=SQL_invoicesQ + "dbo." + table1 + "_Invoice i left join\n"
    SQL_invoicesQ=SQL_invoicesQ + "dbo." + table2 + "_Invoice i2 on i2.TxnID=i.TxnID inner join\n"
    SQL_invoicesQ=SQL_invoicesQ + "dbo." + table1 + "_Customer c on c.ListID=i.CustomerRefListID\n"
    SQL_invoicesQ=SQL_invoicesQ + "where i2.TxnID is null"  

    return SQL_invoicesQ
    """
 
 

SQL_new_customers = """select distinct
ISNULL(c.ParentRefListID,c.ListID) 'ListID', c.BillAddressCity, c.BillAddressAddr1, c.BillAddressAddr2, c.BillAddressAddr3, 
c.BillAddressState, c.Email, c.Fax, c.FirstName, c.LastName,c.Phone, c.AltPhone, c.BillAddressPostalCode
from
dbo.A1_2_Invoice i left join
dbo.A1_Invoice i2 on i2.TxnID = i.TxnID inner join
dbo.A1_2_Customer c on c.ListID = i.CustomerRefListID left join
dbo.A1_Customer c2 on ISNULL(c.ParentRefListID,c.ListID) = ISNULL(c2.ParentRefListID,c2.ListID)
where
i2.TxnID is null and
c2.ListID is null"""

"""
def SQL_new_customersQ(table1,table2):
    #table1='Drummac'
    SQL_new_customersQ="select distinct ISNULL(c.ParentRefListID,c.ListID) 'ListID', c.BillAddressCity, c.BillAddressAddr1, c.BillAddressAddr2, c.BillAddressAddr3,\n"
    SQL_new_customersQ=SQL_new_customersQ + "c.BillAddressState,c.Email,c.Fax,\n"
    SQL_new_customersQ=SQL_new_customersQ + "c.FirstName, c.LastName,\n" 
    SQL_new_customersQ=SQL_new_customersQ + "c.Phone, c.AltPhone, c.BillAddressPostalCode\n"
    SQL_new_customersQ=SQL_new_customersQ + "from\n"
    SQL_new_customersQ=SQL_new_customersQ + "dbo." + table1 + "_Invoice i left join\n"
    SQL_new_customersQ=SQL_new_customersQ + "dbo." + table2 + "_Invoice i2 on i2.TxnID=i.TxnID inner join\n"
    SQL_new_customersQ=SQL_new_customersQ + "dbo." + table1 + "_Customer c on c.ListID=i.CustomerRefListID left join\n"
    SQL_new_customersQ=SQL_new_customersQ + "dbo." + table2 + "_Customer c2 on ISNULL(c.ParentRefListID,c.ListID) = ISNULL(c2.ParentRefListID,c2.ListID)\n"
    SQL_new_customersQ=SQL_new_customersQ + "where i2.TxnID is null and c2.ListID is null"  

    return SQL_new_customersQ
    """



SQL_invoice_line = """select
il.txnID, i.RefNumber, il.CustomerRefListID, il.InvoiceLineAmount, 
il.InvoiceLineDesc, ISNULL(il.InvoiceLineQuantity,1) 'InvoiceLineQuantity', il.InvoiceLineRate,
il.InvoiceLineItemRefFullName, lm.WindRiverID, lm.FullName
from
dbo.A1_2_Invoice i 
inner join
dbo.A1_2_InvoiceLine il on i.TxnID = il.TxnID 
left join
A1_LINEMAPPING lm on il.InvoiceLineItemRefFullName = lm.FullName

left join
dbo.A1_Invoice i2 on i2.TxnID = i.TxnID
where
i2.TxnID is null and InvoiceLineItemRefFullName is not null and 
ISNULL(InvoiceLineAmount,0) <> 0 """


"""
def SQL_invoice_lineQ(table1,table2):
    #table1='Drummac'
    SQL_invoice_lineQ="select il.txnID, i.RefNumber, il.CustomerRefListID, il.InvoiceLineAmount, \n"
    SQL_invoice_lineQ=SQL_invoice_lineQ + "il.InvoiceLineDesc, ISNULL(il.InvoiceLineQuantity,1) 'InvoiceLineQuantity', il.InvoiceLineRate,\n"
    SQL_invoice_lineQ=SQL_invoice_lineQ + "il.InvoiceLineItemRefFullName, lm.WindRiverID, lm.[Wind River Item]\n"
    SQL_invoice_lineQ=SQL_invoice_lineQ + "from\n"
    SQL_invoice_lineQ=SQL_invoice_lineQ + "dbo." + table1 + "_Invoice i inner join\n"
    SQL_invoice_lineQ=SQL_invoice_lineQ + "dbo." + table1 + "_InvoiceLine il on i.TxnID=il.TxnID left join\n"
    SQL_invoice_lineQ=SQL_invoice_lineQ + "dbo." + table2 + "_LINE_MAPPING lm on il.InvoiceLineItemRefFullName = lm.Name left join\n"
    SQL_invoice_lineQ=SQL_invoice_lineQ + "dbo." + table2 + "_Invoice i2 on i2.TxnID = i.TxnID\n"
    SQL_invoice_lineQ=SQL_invoice_lineQ + "where InvoiceLineItemRefFullName is not null and\n"
    SQL_invoice_lineQ=SQL_invoice_lineQ + "ISNULL(InvoiceLineAmount,0) <> 0"  

    return SQL_invoice_lineQ






def SQL_existing_cust_jobsites(table1,table2):
    #table1='Drummac'
    SQL_existing_cust_jobsitesQ="select i.TxnID,js.jobsiteid, js._MarthaJobsiteId, js._MergedJobsite, j.custid,\n"
    SQL_existing_cust_jobsitesQ=SQL_existing_cust_jobsitesQ + "js.addrline1,c.ListID, cc._MarthaCustId, cc._MergedCustomer\n"
    SQL_existing_cust_jobsitesQ=SQL_existing_cust_jobsitesQ + "from\n"
    SQL_existing_cust_jobsitesQ=SQL_existing_cust_jobsitesQ + "dbo." + table1 + "_Invoice i inner join\n"
    SQL_existing_cust_jobsitesQ=SQL_existing_cust_jobsitesQ + "dbo." + table1 + "_Customer c on c.ListID = i.CustomerRefListID left join\n"
    SQL_existing_cust_jobsitesQ=SQL_existing_cust_jobsitesQ + "AcquisitionTools.dbo.customers j on j.oldcustid = ISNULL(c.ParentRefListID,c.ListID) left join\n"
    SQL_existing_cust_jobsitesQ=SQL_existing_cust_jobsitesQ + "dbo." + table2 + "_Invoice i2 on i2.TxnID = i.TxnID left join\n"
    SQL_existing_cust_jobsitesQ=SQL_existing_cust_jobsitesQ + "AcquisitionTools.dbo.jobsites js on j.custid = js.custid left join\n"
    SQL_existing_cust_jobsitesQ=SQL_existing_cust_jobsitesQ + "AcquisitionTools.dbo.customers cc on cc.custid = j.custid\n"  
    SQL_existing_cust_jobsitesQ=SQL_existing_cust_jobsitesQ + "where\n"
    SQL_existing_cust_jobsitesQ=SQL_existing_cust_jobsitesQ + "i2.TxnID is null\n"
    SQL_existing_cust_jobsitesQ=SQL_existing_cust_jobsitesQ + "and j.custid is not null"

    
    return SQL_existing_cust_jobsitesQ"""

SQL_existing_cust_jobsites = """select
i.TxnID,js.jobsiteid, js._MarthaJobsiteId, js._MergedJobsite, j.custid, 
js.addrline1,c.ListID, cc._MarthaCustId, cc._MergedCustomer
from
dbo.A1_2_Invoice i inner join
dbo.A1_2_Customer c on c.ListID = i.CustomerRefListID left join
AcquisitionTools.dbo.customers j on j.oldcustid = ISNULL(c.ParentRefListID,c.ListID) left join
dbo.A1_Invoice i2 on i2.TxnID = i.TxnID left join
AcquisitionTools.dbo.jobsites js on j.custid = js.custid left join
AcquisitionTools.dbo.customers cc on cc.custid = j.custid
where
i2.TxnID is null
and j.custid is not null"""


params_tools = urllib.parse.quote("DRIVER=ODBC Driver 17 for SQL Server;SERVER=WRE-SASAC;DATABASE=AcquisitionTools;trusted_connection=yes;")
engine_tools = create_engine('mssql+pyodbc:///?odbc_connect=%s' % params_tools)
with engine_tools.connect() as cn_tools:
    RAWbillingaddress = pandas.read_sql_table('RAWbillingaddress', cn_tools)
    RAWcustomers = pandas.read_sql_table('RAWcustomers', cn_tools)
    RAWjobsites = pandas.read_sql_table('RAWjobsites', cn_tools)
    RAWorderdetails = pandas.read_sql_table('RAWorderdetails', cn_tools)
    RAWorders = pandas.read_sql_table('RAWorders', cn_tools)
    # load the source tables
    params_sandbox = urllib.parse.quote("DRIVER=ODBC Driver 17 for SQL Server;SERVER=WRE-SASAC;DATABASE=AcquisitionSandbox;trusted_connection=yes;")
    engine_sandbox = create_engine('mssql+pyodbc:///?odbc_connect=%s' % params_sandbox)
    with engine_sandbox.connect() as cn_sandbox:

        invoices = pandas.read_sql(sql=SQL_invoices, con=cn_sandbox)
        invoice_lines = pandas.read_sql(sql=SQL_invoice_line, con=cn_sandbox)
        existing_jobsites = pandas.read_sql(sql=SQL_existing_cust_jobsites, con=cn_sandbox)
        #new_invoices = pandas.read_sql(sql=SQL_invoices_new_customers, con=cn_sandbox)
        new_customers = pandas.read_sql(sql=SQL_new_customers, con=cn_sandbox)
        #RAWorders = pandas.DataFrame(index = np.arange(0, invoices.shape[0]) +np.arange(0, new_invoices.shape[0]), columns = list(RAWorders))
        RAWorders = pandas.DataFrame(index = np.arange(0, invoices.shape[0]), columns = list(RAWorders))
        RAWorderdetails = pandas.DataFrame(index = np.arange(0, invoice_lines.shape[0]), columns = list(RAWorderdetails))

        # Drummac orderid = 9000003
        orderid=2000862
        # Drummac serviceid=15371944
        orderserviceid = 19224018
        #jobsiteid = 0
        #custid = 0


        # TODO: loop through all invoices, using levenshtein distance connect them to jobsite with closest address, based on _merged or _martha jobsiteid's
        for i, ri in invoices.iterrows():
            #get_rows = existing_jobsites.query("TxnID == '" + ri['TxnID'] + "' and (_MarthaJobsiteId == _MarthaJobsiteId or _MergedJobsite == _MergedJobsite)")
            get_rows = existing_jobsites.query("TxnID == '" + ri['TxnID'] + "' or _MarthaJobsiteId == _MarthaJobsiteId")
            #get_rows = existing_jobsites.query("'TxnID== '" + ri['TxnID']")
            #print(i)

            #jobsiteid = 0
            #custid = 0
            min_distance = 100
            for j, rj in get_rows.iterrows():
                #custid = rj['_MarthaCustid'] if rj['_MarthaCustid'] == rj['_MarthaCustId']  else rj['_MergedCustomer']
                custid=rj['custid'] if rj['custid']==rj['custid'] else rj['_MergedCustomer']
                if ri['custaddr1'] is not None:
                    ld = l.distance(rj['addrline1'], ri['custaddr1'])
                    if ld < 10 and ld < min_distance:
                        #jobsiteid = rj['_MarthaJobsiteId'] if rj['_MarthaJobsiteId'] == rj['_MarthaJobsiteId']  else rj['_MergedJobsite']
                        jobsiteid = rj['jobsiteid'] if rj['jobsiteid'] == rj['jobsiteid']  else rj['_MergedJobsite']
                        min_distance = ld
                elif ri['ShipAddressAddr2'] is not None:
                    ld = l.distance(rj['addrline1'], ri['ShipAddressAddr2'])
                    if ld < 10 and ld < min_distance:
                        #jobsiteid = rj['_MarthaJobsiteId'] if rj['_MarthaJobsiteId'] == rj['_MarthaJobsiteId'] else rj['_MergedJobsite']
                        jobsiteid = rj['jobsiteid'] if rj['jobsiteid'] == rj['jobsiteid']  else rj['_MergedJobsite']
                        min_distance = ld
                if jobsiteid == 0:
                    if ri['custaddr1'] is not None:
                        ld = l.distance(rj['addrline1'], ri['custaddr1'])
                        if ld < 10 and ld < min_distance:
                            #jobsiteid = rj['_MarthaJobsiteId'] if rj['_MarthaJobsiteId'] == rj['_MarthaJobsiteId']  else rj['_MergedJobsite']
                            jobsiteid = rj['jobsiteid'] if rj['jobsiteid'] == rj['jobsiteid']  else rj['_MergedJobsite']
                            min_distance = ld
                        elif ri['ShipAddressAddr3'] is not None:
                            ld = l.distance(rj['addrline1'], ri['ShipAddressAddr3'])
                            if ld < 10 and ld < min_distance:
                                #jobsiteid = rj['_MarthaJobsiteId'] if rj['_MarthaJobsiteId'] == rj['_MarthaJobsiteId'] else rj['_MergedJobsite']
                                jobsiteid = rj['jobsiteid'] if rj['jobsiteid'] == rj['jobsiteid']  else rj['_MergedJobsite']
                                min_distance = ld

            RAWorders['orderdate'][i] = ri['ShipDate']
            RAWorders['orderamount'][i] = ri['Subtotal']
            RAWorders['orderponumber'][i] = ri['TxnID']
            RAWorders['jobsiteid'][i] = jobsiteid
            RAWorders['custid'][i] = custid
            orderid = orderid + 1
            RAWorders['orderid'][i] = "DRS" + str(orderid).zfill(7)
            lines = invoice_lines[invoice_lines.txnID == ri.TxnID]

            # added 6/28/18
            for k, rk in lines.iterrows():
                    orderserviceid = orderserviceid + 1
                    RAWorderdetails.orderdetailid[k] = orderserviceid
                    RAWorderdetails.orderid[k] = "DRS" + str(orderid).zfill(7)
                    RAWorderdetails.orderserviceid[k] = rk.WindRiverID
                    RAWorderdetails.orderservicedescription[k] = rk['FullName']
                    RAWorderdetails.orderservicequantity[k] = rk['InvoiceLineQuantity']
                    RAWorderdetails.orderserviceprice[k] = rk.InvoiceLineRate
                    RAWorderdetails.orderservicerevenue[k] = rk.InvoiceLineAmount


        dfc = RAWorders[(RAWorders.custid != 0)][(RAWorders.jobsiteid == 0)]
        for i, ri in dfc.iterrows():
            jobsiteid = existing_jobsites[existing_jobsites._MarthaCustId == ri.custid][existing_jobsites._MarthaJobsiteId == existing_jobsites._MarthaJobsiteId]._MarthaJobsiteId
            #print(i)
            RAWorders.iloc[i]['jobsiteid'] = jobsiteid[jobsiteid.index[0]]

        dfc = RAWorders[(RAWorders.custid == 0)]
        for i, ri in dfc.iterrows():
            ListID = invoices[invoices.TxnID == ri.orderponumber].CustomerRefListID
            ListID = ListID[ListID.index[0]]

        dfc = dfc[dfc.jobsiteid == 0]
        invoices_new_customers = invoices[invoices.TxnID.isin(list(dfc.orderponumber))]
        new_customers = new_customers[new_customers.ListID.isin(invoices_new_customers.CustomerRefListID)]
        new_customers = new_customers.set_index(np.arange(0, new_customers.shape[0]))

        RAWbillingaddress = pandas.DataFrame(index = np.arange(0, new_customers.shape[0]), columns = list(RAWbillingaddress))
        RAWcustomers = pandas.DataFrame(index = np.arange(0, new_customers.shape[0]), columns = list(RAWcustomers))
        RAWjobsites = pandas.DataFrame(index = np.arange(0, new_customers.shape[0]), columns = list(RAWjobsites))

        # Drummac Numbers
        #custid = 106013515
        #jobsiteid = 106014823
        #billingid = 106013663

        # A1 Numbers
        custid=109011506
        jobsiteid=109012467
        billingid=109011551


        def get_phone(phone):
            if phone is not None and phone[:1] != '1':
                return ri.Phone.replace('-','')[:10] 
            elif phone is not None:
                return ri.Phone.replace('-','')[1:9] 
            else:
                return phone

        for i, ri in new_customers.iterrows():
            custid = custid + 1
            RAWcustomers.custid[i] = custid
            #RAWcustomers.custacquisitionid[i] = 106
            RAWcustomers.custacquisitionid=109
            RAWcustomers.custaddcity[i] = ri.BillAddressCity
            RAWcustomers.custaddress1[i] = ri.BillAddressAddr2
            RAWcustomers.custaddress2[i] = ri.BillAddressAddr3
            RAWcustomers.custaddstate[i] = ri.BillAddressState
            RAWcustomers.custaddzip[i] = ri.BillAddressPostalCode[:5] if ri.BillAddressPostalCode is not None else ri.BillAddressPostalCode
            RAWcustomers.custlastname[i] = ri.BillAddressAddr1
            #RAWcustomers.custlastname[i]=ri.LastName
            RAWcustomers.custfirstname[i] = ri.FirstName
            RAWcustomers.custcategoryid[i] = 1
            RAWcustomers.custprimaryphone[i] = get_phone(ri.Phone)
            #RAWcustomers.custprimaryphone[i] = ri.Phone
            RAWcustomers.custprimaryphoneext[i] = ri.Phone[-3:] if ri.Phone is not None and 'ext' in ri.Phone else None
            RAWcustomers.custsecondaryphone[i] = ri.AltPhone
            RAWcustomers.custshowprice[i] = True
            RAWcustomers.oldcustid[i] = ri.ListID

            billingid = billingid + 1
            RAWbillingaddress.billingid[i] = billingid
            RAWbillingaddress.custid[i] = custid
            RAWbillingaddress.billto[i] = ri.BillAddressAddr1
            RAWbillingaddress.billingaddress1[i] = ri.BillAddressAddr2
            RAWbillingaddress.billingaddress2[i] = ri.BillAddressAddr3
            RAWbillingaddress.billingaddcity[i] = RAWcustomers.custaddcity[i]
            RAWbillingaddress.billingaddzip[i] = RAWcustomers.custaddzip[i]
            RAWbillingaddress.billingaddstate[i] = RAWcustomers.custaddstate[i]
            RAWbillingaddress.billingphone[i] = RAWcustomers.custprimaryphone[i]
            RAWbillingaddress.billingphoneextn[i] = RAWcustomers.custprimaryphoneext[i]
            RAWbillingaddress.billingemail[i] = RAWcustomers.custemail[i]
            RAWbillingaddress.oldbillingid[i] = RAWcustomers.oldcustid[i]

            jobsiteid = jobsiteid + 1
            RAWjobsites.jobsiteid[i] = jobsiteid
            RAWjobsites.custid[i] = custid
            RAWjobsites.billingid[i] = billingid
            RAWjobsites.jobsitecontact[i] = RAWcustomers.custlastname[i]
            RAWjobsites.jobsitename[i] = 'Jobsite'
            RAWjobsites.jobsiteaddrline1[i] = RAWcustomers.custaddress1[i]
            RAWjobsites.jobsiteaddrline2[i] = RAWcustomers.custaddress2[i]
            RAWjobsites.jobsiteaddcity[i] = RAWcustomers.custaddcity[i]
            RAWjobsites.jobsiteaddzip[i] = RAWcustomers.custaddzip[i]
            RAWjobsites.jobsiteaddstate[i] = RAWcustomers.custaddstate[i]
            RAWjobsites.jobsitephone[i] = RAWcustomers.custprimaryphone[i]
            RAWjobsites.jobsitephonext[i] = RAWcustomers.custprimaryphoneext[i]
            RAWjobsites.oldjobsiteid[i] = RAWcustomers.oldcustid[i]

            current_cust_invoices = invoices_new_customers[invoices_new_customers.CustomerRefListID == RAWcustomers.oldcustid[i]]
            for j, rj in current_cust_invoices.iterrows():
                RAWorders['orderdate'][j] = rj['ShipDate']
                RAWorders['orderamount'][j] = rj['Subtotal']
                RAWorders['orderponumber'][j] = rj['TxnID']
                RAWorders['jobsiteid'][j] = jobsiteid
                RAWorders['custid'][j] = custid
                orderid = orderid + 1
                RAWorders['orderid'][j] = "DRS" + str(orderid).zfill(7)
                lines = invoice_lines[invoice_lines.txnID == rj.TxnID]
                for k, rk in lines.iterrows():
                    orderserviceid = orderserviceid + 1
                    RAWorderdetails.orderdetailid[k] = orderserviceid
                    RAWorderdetails.orderid[k] = RAWorders['orderid'][j]
                    RAWorderdetails.orderserviceid[k] = rk.WindRiverID
                    RAWorderdetails.orderservicedescription[k] = rk['FullName']
                    RAWorderdetails.orderservicequantity[k] = rk['InvoiceLineQuantity']
                    RAWorderdetails.orderserviceprice[k] = rk.InvoiceLineRate
                    RAWorderdetails.orderservicerevenue[k] = rk.InvoiceLineAmount


