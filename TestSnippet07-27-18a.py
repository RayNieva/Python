import pandas
import Levenshtein as l
from sqlalchemy import create_engine
import urllib
import numpy as np


    
SQL_jobsites="""select
'' as jobsiteid
, rc.custid as custid
, b.billingid as billingid
, rc.custlastname as contact
, 'Jobsite' as jobsitename


,c.BillAddressAddr1
,c.ShipAddressAddr1

,c.BillAddressAddr2
,c.ShipAddressAddr2

,c.BillAddressCity
,c.ShipAddressCity

,c.BillAddressState
,c.ShipAddressState

,c.BillAddressPostalCode
,c.ShipAddressPostalCode
,rc.custprimaryphone
,rc.custprimaryphoneext
,rc.oldcustid




from [dbo].[OXB_Customer] c
left join
AcquisitionTools.dbo.RAWcustomers rc
on c.ListID=rc.oldcustid
left join
AcquisitionTools.dbo.RAWbillingaddress b
on b.custid=rc.custid

order by ShipAddressAddr1
"""

params_tools = urllib.parse.quote("DRIVER=ODBC Driver 13 for SQL Server;SERVER=WRE-SASAC;DATABASE=AcquisitionTools;trusted_connection=yes;")
engine_tools = create_engine('mssql+pyodbc:///?odbc_connect=%s' % params_tools)
with engine_tools.connect() as cn_tools:
    
    RAWcustomers = pandas.read_sql_table('RAWcustomers', cn_tools)
    RAWbillingaddress = pandas.read_sql_table('RAWbillingaddress', cn_tools)
    RAWjobsites = pandas.read_sql_table('RAWjobsites', cn_tools)
    
    #RAWorders = pandas.read_sql_table('RAWorders', cn_tools)
    #RAWorderdetails = pandas.read_sql_table('RAWorderdetails', cn_tools)
    #RAWinteractions = pandas.read_sql_table('RAWinteractions', cn_tools)

    # load the source tables
    params_sandbox = urllib.parse.quote("DRIVER=ODBC Driver 13 for SQL Server;SERVER=WRE-SASAC;DATABASE=AcquisitionSandbox;trusted_connection=yes;")
    engine_sandbox = create_engine('mssql+pyodbc:///?odbc_connect=%s' % params_sandbox)
    with engine_sandbox.connect() as cn_sandbox:

        
        jobsites = pandas.read_sql(sql=SQL_jobsites, con=cn_sandbox)
        RAWjobsites=pandas.DataFrame(index = np.arange(0, jobsites.shape[0]), columns = list(RAWjobsites))
        print(RAWjobsites.shape)
        jobsiteid=0  

        for i, ri in jobsites.iterrows():
            print('i' , i, jobsiteid)
            



            jobsiteid = jobsiteid + 1
            RAWjobsites.jobsiteid[i] = jobsiteid
            RAWjobsites.custid[i] = ri['custid']


            RAWjobsites.billingid[i] = ri['billingid']
            RAWjobsites.jobsitecontact[i] = RAWcustomers.custlastname[i]
            RAWjobsites.jobsitename[i] = 'Jobsite'
            ld=l.distance(ri['BillAddress1',ri['ShipAddressAddr1'])
