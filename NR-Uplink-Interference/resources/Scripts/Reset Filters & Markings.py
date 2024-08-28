from Spotfire.Dxp.Data import RowSelection,  IndexSet
from System.Collections.Generic import List,  Dictionary
from Spotfire.Dxp.Application.Visuals import Visualization, VisualTypeIdentifiers
from Spotfire.Dxp.Application import Filters as filters
        
def reset_marking_and_filtering():	
    for data_table in Document.Data.Tables: 
        for marking in Document.Data.Markings: 
            rows = RowSelection(IndexSet(data_table.RowCount,  False))
            marking.SetSelection(rows,  data_table)              
        for filter_scheme in Document.FilteringSchemes: 
            filter_scheme.ResetAllFilters()

def reset_document_properties():
	Document.Properties["SelectedNode"] = ""
	Document.Properties["MultipleNodeError"] = ""
	Document.Properties["MeasureSelectionPageNT"]=1
	Document.Properties["NameWorkAroundNT"]="Interference Power (dBm)"
	Document.Properties["AggregationSelectionNT"]="Avg"
	Document.Properties["MeasureSelectionPage1"]=1
	Document.Properties["NameWorkAround"]="Interference Power (dBm)"
	Document.Properties["AggregationSelection"]="Avg"
	Document.Properties["NodeSlider"]=10
	Document.Properties["MeasureSelectionPagePRBHC"]=1
	Document.Properties["NameWorkAroundPRBHC"]="Interference Power (dBm)"
	Document.Properties["AggregationSelectionPRBHC"]="Avg"
	Document.Properties["MeasureSelectionPagePUSCHHC"]=1
	Document.Properties["NameWorkAroundPUSCHHC"]="Interference Power (dBm)"
	Document.Properties["AggregationSelectionPUSCHHC"]="Avg"
	Document.Properties["CellSelection"]=""
	Document.Properties["CellSelectionPRB2"]=""
	Document.Properties["Alertmsg"]= ""

def reset_dod_tables():
	Document.Data.Tables.Refresh([Document.Data.Tables['IL_DC_E_NRCELLDU_V_RAW_DoD_Node']])
	Document.Data.Tables.Refresh([Document.Data.Tables['IL_DC_E_NRCELLDU_V_RAW_PRB_DoD']])
	Document.Data.Tables.Refresh([Document.Data.Tables['IL_DC_E_NR_NRCELLDU_V_RAW_PUSCH_DoD']])


reset_marking_and_filtering()
reset_document_properties()
reset_dod_tables()
 

