from django.db.models import Model
from typing import Any, List
import pandas as pd


class DataframeFromModel:
    """Generate pandas dataframe from model"""

    def __init__(self, model: Model):
        self.model = model

    def get_fields(self, field_lables: List):
        """Get model field values.

        Args:
            `field_lables` (List): arbitrary fields as defined in the model.
            Note: Must be a list of existing model fields.

        Returns:
            list of dict objects.
            - key(s): model field
            - values(s): model field values
        """
        return list(self.model.objects.values(*field_lables))

    def get_dataframe(self, field_lables: List, index: Any = None):
        """Generate pandas dataframe

        Args:
            `field_lables` (List): arbitrary fields as defined in the model.
            `index` (Any, optional): dataframe index. Defaults to None.
            if index is None, `field_lables[0]` will be used as index.

        Returns:
            `pandas DataFrame`
        """
        columns = list(self.get_fields(field_lables)[0].keys())
        data = [list(dict_data.values()) for dict_data in self.get_fields(field_lables)]
        df = pd.DataFrame(data, columns=columns)

        if index:
            df.set_index(index, inplace=True)
        else:
            df.set_index(field_lables[0], inplace=True)
        return df
