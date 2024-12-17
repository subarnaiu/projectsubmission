import arcpy
import arcpy.mapping

arcpy.env.workspace=r'E:\EDGE_208\input'

arcpy.env.overwriteOutput=True

shape_data=arcpy.ListFeatureClasses()
print(shape_data)
point_data=r'E:\EDGE_208\input\buildings.shp'#point_data=shape_data[4]
buffer_distance='235 Meters'
buffer_output=r'E:\EDGE_208\output\point buffer\point_out.shp'
arcpy.Buffer_analysis(point_data,buffer_output,buffer_distance,dissolve_option='All')

pdf_output=r'E:\EDGE_208\buffer map output\pointmap_intersection.pdf'
road=r'E:\EDGE_208\input\roads.shp'

mxd_path= r'E:\EDGE_208\map\blankmap.mxd'
intersect_out=r'E:\EDGE_208\output\intersection\intersect_out.shp'

arcpy.Intersect_analysis([buffer_output,road],intersect_out)
print('Intersection analysis Successful')

mxd=arcpy.mapping.MapDocument(mxd_path)
df=arcpy.mapping.ListDataFrames(mxd)[0]
point_layer=arcpy.mapping.Layer(buffer_output)

intersection_layer=arcpy.mapping.Layer(intersect_out)
arcpy.mapping.AddLayer(df,point_layer,add_position='TOP')
arcpy.mapping.AddLayer(df,intersection_layer,add_position="TOP")
arcpy.mapping.ExportToPDF(mxd,pdf_output)