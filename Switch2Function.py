#;; This buffer is for text that is not saved, and for Lisp evaluation.
#;; To create a file, visit it with C-x C-f and enter text in its buffer.

def f(x):
    return {
        'a': 1,
        'b': 2
    }
    }.get(x, 9)    # 9 is default if x not found


def custid(x):
    return {
        if rj['_MarthaCustid']=rj['_MarthaCustid']:rj['_MarthaCustid'],
        else rj['_MarthaCustid']:''
    }
      


existing_jobsites = pandas.read_sql(sql=SQL_existing_cust_jobsites, con=cn_sandbox)

for i, ri in invoices.iterrows():
    get_rows = existing_jobsites.query("TxnID == '" + ri['TxnID'] + "' and (_MarthaJobsiteId == _MarthaJobsiteID or _MergedJobsite == MergedJobsite)"))
