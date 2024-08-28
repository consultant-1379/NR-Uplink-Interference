from Spotfire.Dxp.Data import DataTable
table=Document.Data.Tables["MarkedCellsPRB"]
column=table.Columns["MarkedCellsPRB"]
rowValues=column.RowValues
if rowValues.Count!=0:
	Document.ActivePageReference=Document.Pages[5]
	Document.Properties["Alertmsg"]= ""
else:
	Document.Properties["Alertmsg"]= "Please mark the Node(s) from Worst "  +str(Document.Properties["NodeSlider"]) +" Cells" +" by " +Document.Properties["AggregationSelection"] +" PUSCH "+Document.Properties["NameWorkAround"] +" per PRB chart " +"\n" + "to view the detailed information in PRB Analysis page."