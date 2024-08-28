from Spotfire.Dxp.Data import DataTable

sourceDataTable = Document.Data.Tables["IL_DC_E_NR_NRCELLDU_V_DAY_PUSCH"]
dataFilteringSelection = Document.Data.Filterings["Filtering scheme Node Troubleshooting"]
filteringScheme = Document.FilteringSchemes[dataFilteringSelection]
filterCollection = filteringScheme[sourceDataTable]
filter = filterCollection['NR_NAME']

if (',' in filter.ToString()) or '((All))' in filter.ToString():
    Document.Properties["MultipleNodeError"] = "Please select only one node"
else : 
    Document.Properties["MultipleNodeError"] = ""
    Document.Properties["SelectedNode"] = ((filter.ToString()).split(':')[1]).replace('(','').replace(')','').strip()
    Document.Data.Tables.Refresh([Document.Data.Tables['IL_DC_E_NRCELLDU_V_RAW_DoD_Node']])       