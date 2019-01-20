for i, ri in invoices.iterrows():
            #get_rows = existing_jobsites.query("TxnID == '" + ri['TxnID'] + "' and (_MarthaJobsiteId == _MarthaJobsiteId or _MergedJobsite == _MergedJobsite)")
            get_rows = existing_jobsites.query("TxnID == '" + ri['TxnID'] + "' and _MarthaJobsiteId == _MarthaJobsiteId")
            #print(i)

            jobsiteid = 0
            custid = 0
            min_distance = 100
            for j, rj in get_rows.iterrows():
                custid = rj['_MarthaCustId'] if rj['_MarthaCustId'] == rj['_MarthaCustId']  else rj['_MergedCustomer']
                if ri['custaddr1'] is not None:
                    ld = l.distance(rj['addrline1'], ri['custaddr1'])
                    if ld < 10 and ld < min_distance:
                        jobsiteid = rj['_MarthaJobsiteId'] if rj['_MarthaJobsiteId'] == rj['_MarthaJobsiteId']  else rj['_MergedJobsite']
                        min_distance = ld
                elif ri['ShipAddressAddr2'] is not None:
                    ld = l.distance(rj['addrline1'], ri['ShipAddressAddr2'])
                    if ld < 10 and ld < min_distance:
                        jobsiteid = rj['_MarthaJobsiteId'] if rj['_MarthaJobsiteId'] == rj['_MarthaJobsiteId'] else rj['_MergedJobsite']
                        min_distance = ld
                if jobsiteid == 0:
                    if ri['custaddr1'] is not None:
                        ld = l.distance(rj['addrline1'], ri['custaddr1'])
                        if ld < 10 and ld < min_distance:
                            jobsiteid = rj['_MarthaJobsiteId'] if rj['_MarthaJobsiteId'] == rj['_MarthaJobsiteId']  else rj['_MergedJobsite']
                            min_distance = ld
                        elif ri['ShipAddressAddr3'] is not None:
                            ld = l.distance(rj['addrline1'], ri['ShipAddressAddr3'])
                            if ld < 10 and ld < min_distance:
                                jobsiteid = rj['_MarthaJobsiteId'] if rj['_MarthaJobsiteId'] == rj['_MarthaJobsiteId'] else rj['_MergedJobsite']
                                min_distance = ld
