class View:
    
    @staticmethod
    def create_collect_view(data,collect_set):

        """
        Creates a view for the instances of collection.

        @type data: dict
        @param data: The uploaded input data

        @type collect_set: set
        @param collect_set: A set of every instance of data collection

        @rtype collect_view: dict
        @return collect_view: A data structure representing the collection views.
        The keys are instance of data collection, the values are the properties of that data collection.
        """

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
