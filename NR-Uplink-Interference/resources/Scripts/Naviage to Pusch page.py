from Spotfire.Dxp.Data import DataTable
table=Document.Data.Tables["MarkedCells"]
column=table.Columns["y"]
rowValues=column.RowValues
if rowValues.Count!=0:
	Document.Properties["Alertmsg"]=""
	Document.ActivePageReference=Document.Pages[2]
else:
	Document.Properties["Alertmsg"]= Document.Properties["Alertmsg"]= "Please mark the Node(s) from Worst "  +str(Document.Properties["NodeSlider"]) +" Cells"+" by " +Document.Properties["AggregationSelection"] +" PUSCH "+Document.Properties["NameWorkAround"] +" chart " +"\n" + "to view the detailed information in PUSCH Analysis page."