import csv 
import pandas as pd 
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects 

df =pd.read_csv('height-weight.csv')

heightList=df['Height(Inches)'].to_list()
weightList= df['Weight(Pounds)'].to_list()

height_mean=statistics.mean(heightList)
weight_mean=statistics.mean(weightList)

height_median=statistics.median(heightList)
weight_median=statistics.median(weightList)

height_mode=statistics.mode(heightList)
weight_mode= statistics.mode(weightList)


print(height_mean, height_median, height_mode, weight_mean, weight_median, weight_mode)

#fig= ff.create_distplot([df['Height(Inches)']],'Height')
#fig.show()

height_sd=statistics.stdev(heightList)
weight_sd=statistics.stdev(weightList)

height_1_start , height_1_end = height_mean - height_sd , height_mean + height_sd
height_2_start , height_2_end = height_mean - (2*height_sd) , height_mean + (2*height_sd)
height_3_start , height_3_end = height_mean - (3*height_sd) , height_mean + (3*height_sd)

weight_1_start , weight_1_end = weight_mean - weight_sd , weight_mean + weight_sd
weight_2_start , weight_2_end = weight_mean - (2*weight_sd) , weight_mean + (2*weight_sd)
weight_3_start , weight_3_end = weight_mean - (3*weight_sd) , weight_mean + (3*weight_sd)

heightList_1 =[result for result in heightList if result > height_1_start and result < height_1_end]
heightList_2 =[result for result in heightList if result > height_2_start and result < height_2_end]
heightList_3 =[result for result in heightList if result > height_3_start and result < height_3_end]

weightList_1 =[result for result in weightList if result > weight_1_start and result < weight_1_end]
weightList_2=[result for result in weightList if result > weight_2_start and result < weight_2_end]
weightList_3 =[result for result in weightList if result > weight_3_start and result < weight_3_end]

print('{}% of data for height lies within 1 sd'.format(len(heightList_1)*100.10/len(heightList)))
print('{}% of data for height lies within 2 sd'.format(len(heightList_2)*100.10/len(heightList)))
print('{}% of data for height lies within 3 sd'.format(len(heightList_3)*100.10/len(heightList)))

print('{}% of data for weight lies within 1 sd'.format(len(weightList_1)*100.10/len(weightList)))
print('{}% of data for weight lies within 2 sd'.format(len(weightList_2)*100.10/len(weightList)))
print('{}% of data for weight lies within 3 sd'.format(len(weightList_3)*100.10/len(weightList)))

