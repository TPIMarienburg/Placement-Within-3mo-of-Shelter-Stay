import pandas as pd
import numpy as np

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

class IdentifyPlacementsPostShelterStay:
    """
    This class will process the Placement Report v.4 + Entry to Shelter.xlsx report that is an ART
    product.

    The goal is to create a list of addresses for participants who were placed into housing within
    3 months of a shelter stay.
    """
    def __init__(self, file):
        self.file = file
        self.raw_entries = pd.read_excel(self.file, sheet_name="Entries to Shelter")
        self.raw_placements = pd.read_excel(self.file, sheet_name="Placement Data")
        self.raw_addresses = pd.read_excel(self.file, sheet_name="Address Data")

    def find_related_data(
        self,
        entries=self.entries,
        placements=self.placements,
        adresses=self.addresses
    ):
        """
        Compare the entries dataframe and the placement dataframe. Return a placement dataframe with
        at least one related row in the entries dataframe.  Also return an entry dataframe with at
        least a single value in the placement dataframe, and an address dataframe with at least a
        single value in the placement dataframe.

        :entries: The raw_entries dataframe
        :placements: The raw_placements dataframe
        :addresses:  The raw_adresses dataframe
        """
        pass

    def check_for_entry_3_months_prior_to_placement(self, entry_data, placement_data):
        """
        Compare shelter exit dates and placement dates looking for an entry exit exit date that is
        no more than 3 months prior to the placement date.  Return the resulting placement
        dataframe.

        :entry_data: An entry dataframe processed to only contain rows with a Client Uid in the
        placement dataframe
        :placement_data: A placement dataframe processed to only contain rows with a Client Uid in the
        entries dataframe
        """
        pass

    def find_closest_address(self, placement_data):
        """
        Compare the addresses dataframe to the placements dataframe returned by the
        check_for_entry_3_months_prior_to_placement method and return a dataframe of addresses that
        have a start date which is closest to, but not greater than, the placement date.

        :placement_data: The placement dataframe output by the
        check_for_entry_3_months_prior_to_placement methodself.
        :address_data: The address data_frame that is produced by the find_related_data method.
        """
        pass

    def process(self):
        """
        Call the other methods in this class in sequence and return the resulting dataframe.
        Sequence: find_related_data, check_for_entry_3_months_prior_to_placement,
        find_closest_address
        """
        entry_data, placement_data, address_data = self.find_related_data()
        post_shelter_placement = self.check_for_entry_3_months_prior_to_placement(
            entry_data,
            placement_data
        )
        return find_closest_address(post_shelter_placement)

if __name__ == "__main__":
    report = askopenfilename(
        title="Open the Placement Report v.4 + Entry to Shelter.xlsx ART report"
    )
    run = IdentifyPlacementsPostShelterStay(report)
    report = run.process()
    writer = pd.ExcelWriter(
        asksaveasfilename(
            title="Save the Shelter Related Placement Report",
            defaultextension=".xlsx",
            initialfile="Shelter Related Placement Report"
        ),
        engine="xlsxwriter"
    )
