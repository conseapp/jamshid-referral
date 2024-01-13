from datetime import datetime

from import_export import resources
from .models import Referral


class ReferralResource(resources.ModelResource):
    class Meta:
        model = Referral

    # def before_import(self, dataset, using_transactions, dry_run, **kwargs):
    #     # Access and modify the data in the dataset here
    #     modified_data = []
    #     print(dataset)
    #     for row in dataset:
    #         print(row)
    #         modified_list = list(row)
    #         new_value = datetime.strptime(row[0],
    #                                       "%Y-%m-%dT%H:%M:%SZ")
    #         modified_list[0] = new_value
    #         modified_tuple = tuple(modified_list)
    #         print(modified_tuple)
    #         row = modified_tuple
    #
    #     print(dataset)
    #     super().before_import(dataset, using_transactions, dry_run, **kwargs)
