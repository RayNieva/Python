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
dbo.Drummac2_Invoice i left join
dbo.Drummac_Invoice i2 on i2.TxnID = i.TxnID inner join
dbo.Drummac2_Customer c on c.ListID = i.CustomerRefListID
where
i2.TxnID is null"""

def sql_invoicesQ(table1,table2):
    """
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
    """
    
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
 

def sql_invoices(table1,table2):
    """
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
    """
    
    #table1='Drummac'
    SQL_invoices="select i.TxnID, i.RefNumber, I.ShipDate, I.Subtotal, i.CustomerRefListID, "
    SQL_invoices=SQL_invoices + "i.ShipAddressAddr2,i.ShipAddressAddr3,i.ShipAddressAddr4, "
    SQL_invoices=SQL_invoices + "c.ShipAddressAddr1 'custaddr1', c.ShipAddressAddr2 'custaddr2', " 
    SQL_invoices=SQL_invoices + "c.ShipAddressAddr3 'custaddr3', c.ShipAddressAddr4 'custaddr4' "
    SQL_invoices=SQL_invoices + "from "
    SQL_invoices=SQL_invoices + "dbo." + table1 + "_Invoice i left join "
    SQL_invoices=SQL_invoices + "dbo." + table2 + "_Invoice i2 on i2.TxnID=i.TxnID inner join "
    SQL_invoices=SQL_invoices + "dbo." + table1 + "_Customer c on c.ListID=i.CustomerRefListID "
    SQL_invoices=SQL_invoices + "where i2.TxnID is null"  

    return SQL_invoices
 



SQL_new_customers = """select distinct
ISNULL(c.ParentRefListID,c.ListID) 'ListID', c.BillAddressCity, c.BillAddressAddr1, c.BillAddressAddr2, c.BillAddressAddr3, 
c.BillAddressState, c.Email, c.Fax, c.FirstName, c.LastName,c.Phone, c.AltPhone, c.BillAddressPostalCode
from
dbo.Drummac2_Invoice i left join
dbo.Drummac_Invoice i2 on i2.TxnID = i.TxnID inner join
dbo.Drummac2_Customer c on c.ListID = i.CustomerRefListID left join
dbo.Drummac_Customer c2 on ISNULL(c.ParentRefListID,c.ListID) = ISNULL(c2.ParentRefListID,c2.ListID)
where
i2.TxnID is null and
c2.ListID is null"""

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


def SQL_new_customers(table1,table2):
    #table1='Drummac'
    SQL_new_customers="select distinct ISNULL(c.ParentRefListID,c.ListID) 'ListID', c.BillAddressCity, c.BillAddressAddr1, c.BillAddressAddr2, c.BillAddressAddr3,\n"
    SQL_new_customers=SQL_new_customers + "c.BillAddressState,c.Email,c.Fax, "
    SQL_new_customers=SQL_new_customers + "c.FirstName, c.LastName, " 
    SQL_new_customers=SQL_new_customers + "c.Phone, c.AltPhone, c.BillAddressPostalCode "
    SQL_new_customers=SQL_new_customers + "from "
    SQL_new_customers=SQL_new_customers + "dbo." + table1 + "_Invoice i left join "
    SQL_new_customers=SQL_new_customers + "dbo." + table2 + "_Invoice i2 on i2.TxnID=i.TxnID inner join "
    SQL_new_customers=SQL_new_customers + "dbo." + table1 + "_Customer c on c.ListID=i.CustomerRefListID left join "
    SQL_new_customers=SQL_new_customers + "dbo." + table2 + "_Customer c2 on ISNULL(c.ParentRefListID,c.ListID) = ISNULL(c2.ParentRefListID,c2.ListID) "
    SQL_new_customers=SQL_new_customers + "where i2.TxnID is null and c2.ListID is null"  

    return SQL_new_customers





    SQL_invoice_line = """select
il.txnID, i.RefNumber, il.CustomerRefListID, il.InvoiceLineAmount, 
il.InvoiceLineDesc, ISNULL(il.InvoiceLineQuantity,1) 'InvoiceLineQuantity', il.InvoiceLineRate,
il.InvoiceLineItemRefFullName, lm.WindRiverID, lm.[Wind River Item]

from
dbo.Drummac2_Invoice i 
inner join
dbo.Drummac2_InvoiceLine il on i.TxnID = il.TxnID 
left join
Drummac_LINE_MAPPING lm on il.InvoiceLineItemRefFullName = lm.Name  

left join
dbo.Drummac_Invoice i2 on i2.TxnID = i.TxnID
where
i2.TxnID is null and InvoiceLineItemRefFullName is not null and 
ISNULL(InvoiceLineAmount,0) <> 0 """





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


def SQL_invoice_line(table1,table2):
    #table1='Drummac'
    SQL_invoice_line="select il.txnID, i.RefNumber, il.CustomerRefListID, il.InvoiceLineAmount, "
    SQL_invoice_line=SQL_invoice_line + "il.InvoiceLineDesc, ISNULL(il.InvoiceLineQuantity,1) 'InvoiceLineQuantity', il.InvoiceLineRate, "
    SQL_invoice_line=SQL_invoice_line + "il.InvoiceLineItemRefFullName, lm.WindRiverID, lm.[Wind River Item] "
    SQL_invoice_line=SQL_invoice_line + "from\n"
    SQL_invoice_line=SQL_invoice_line + "dbo." + table1 + "_Invoice i inner join "
    SQL_invoice_line=SQL_invoice_line + "dbo." + table1 + "_InvoiceLine il on i.TxnID=il.TxnID left join "
    SQL_invoice_line=SQL_invoice_line + "dbo." + table2 + "_LINE_MAPPING lm on il.InvoiceLineItemRefFullName = lm.Name left join "
    SQL_invoice_line=SQL_invoice_line + "dbo." + table2 + "_Invoice i2 on i2.TxnID = i.TxnID  "
    SQL_invoice_line=SQL_invoice_line + "where InvoiceLineItemRefFullName is not null and "
    SQL_invoice_line=SQL_invoice_line + "ISNULL(InvoiceLineAmount,0) <> 0"  

    return SQL_invoice_line




SQL_existing_cust_jobsites = """select
i.TxnID,js.jobsiteid, js._MarthaJobsiteId, js._MergedJobsite, j.custid, 
js.addrline1,c.ListID, cc._MarthaCustId, cc._MergedCustomer
from
dbo.Drummac2_Invoice i inner join
dbo.Drummac2_Customer c on c.ListID = i.CustomerRefListID left join
AcquisitionTools.dbo.customers j on j.oldcustid = ISNULL(c.ParentRefListID,c.ListID) left join
dbo.Drummac_Invoice i2 on i2.TxnID = i.TxnID left join
AcquisitionTools.dbo.jobsites js on j.custid = js.custid left join
AcquisitionTools.dbo.customers cc on cc.custid = j.custid
where
i2.TxnID is null
and j.custid is not null"""


def SQL_existing_cust_jobsitesQ(table1,table2):
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

    
    return SQL_existing_cust_jobsitesQ


def SQL_existing_cust_jobsites(table1,table2):
    #table1='Drummac'
    SQL_existing_cust_jobsites="select i.TxnID,js.jobsiteid, js._MarthaJobsiteId, js._MergedJobsite, j.custid, "
    SQL_existing_cust_jobsites=SQL_existing_cust_jobsites + "js.addrline1,c.ListID, cc._MarthaCustId, cc._MergedCustomer "
    SQL_existing_cust_jobsites=SQL_existing_cust_jobsites + "from "
    SQL_existing_cust_jobsites=SQL_existing_cust_jobsites + "dbo." + table1 + "_Invoice i inner join "
    SQL_existing_cust_jobsites=SQL_existing_cust_jobsites + "dbo." + table1 + "_Customer c on c.ListID = i.CustomerRefListID left join "
    SQL_existing_cust_jobsites=SQL_existing_cust_jobsites + "AcquisitionTools.dbo.customers j on j.oldcustid = ISNULL(c.ParentRefListID,c.ListID) left join "
    SQL_existing_cust_jobsites=SQL_existing_cust_jobsites + "dbo." + table2 + "_Invoice i2 on i2.TxnID = i.TxnID left join "
    SQL_existing_cust_jobsites=SQL_existing_cust_jobsites + "AcquisitionTools.dbo.jobsites js on j.custid = js.custid left join "
    SQL_existing_cust_jobsites=SQL_existing_cust_jobsites + "AcquisitionTools.dbo.customers cc on cc.custid = j.custid "  
    SQL_existing_cust_jobsites=SQL_existing_cust_jobsites + "where "
    SQL_existing_cust_jobsites=SQL_existing_cust_jobsites + "i2.TxnID is null "
    SQL_existing_cust_jobsites=SQL_existing_cust_jobsites + "and j.custid is not null"

    
    return SQL_existing_cust_jobsites


