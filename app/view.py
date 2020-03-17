

class View:


    @staticmethod
    def create_collect_view(data,collect_set):

        collect_view = {}
        for collect in collect_set:
            collect_view[collect] = {}

        for key in collect_view:
            collect_view[key] = {"PersonalDataCategory":set(),
                                "Purpose":set(),
                                "Processing":set(),
                                "Recipient":set(),
                                "StorageLocation":set(),
                                "StorageDuration":set()}

            for cat in data["dpv:PersonalDataHandling"]:
                if(key in cat["dpv:Collect"]):
                    collect_view[key]["PersonalDataCategory"].add(cat["dpv:hasPersonalDataCategory"])
                    collect_view[key]["Purpose"].update(cat["dpv:hasPurpose"])
                    collect_view[key]["Processing"].update(cat["dpv:hasProcessing"])
                    collect_view[key]["Recipient"].update(cat["dpv:hasRecipient"])
                    collect_view[key]["StorageLocation"].add(cat["dpv:StorageLocation"])
                    collect_view[key]["StorageDuration"].add(cat["dpv:StorageDuration"])

        return collect_view

    @staticmethod
    def create_purpose_view(data,purpose_set):

        purpose_view = {}
        for purpose in purpose_set:
            purpose_view[purpose] = {}

        for key in purpose_view:
            purpose_view[key] = {"PersonalDataCategory":set(),
                                "Processing":set(),
                                "Recipient":set(),}

            for cat in data["dpv:PersonalDataHandling"]:
                if(key in cat["dpv:hasPurpose"]):
                    purpose_view[key]["PersonalDataCategory"].add(cat["dpv:hasPersonalDataCategory"])
                    purpose_view[key]["Processing"].update(cat["dpv:hasProcessing"])
                    purpose_view[key]["Recipient"].update(cat["dpv:hasRecipient"])

        return purpose_view