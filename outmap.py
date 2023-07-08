import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import BMap
from pyecharts.globals import BMapType
import json
from os import system,getcwd

path = getcwd()#获取当前路径
 
#path+".\try2.xlsx"
data=pd.read_excel(path+"\\go_pla_count.xlsx")

hotmap = (
    BMap(is_ignore_nonexistent_coord=True,    #忽略不存在的坐标
         init_opts=opts.InitOpts(width="1920px", height="1080px"))
    .add_schema(baidu_ak="Z57V9fvCDuGNGBlLaLtRn95o1oD3ovFc", center=[120.13066322374, 30.240018034923],
                zoom=5,   # 当前视角的缩放比例
                is_roam=True   # 是否开启鼠标缩放和平移漫游
               )  
    .add(
        "人数",  #图例
        data_pair=[list(z) for z in zip(data['地区'].to_list(), data['人数'].to_list())],
        type_="heatmap",
        label_opts=opts.LabelOpts(formatter="{a}"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="轻微缩放后准确显示,5人及以上地区为最高值",
                                  pos_left='center',
                                  title_textstyle_opts=opts.TextStyleOpts(font_size=16)
                                 ), 
        legend_opts=opts.LegendOpts(pos_right='20%'),
        visualmap_opts=opts.VisualMapOpts(max_=4, range_color=['#00FF00', '#2E9AFE'])


    )
    .add_control_panel(
        copyright_control_opts=opts.BMapCopyrightTypeOpts(position=3),
        maptype_control_opts=opts.BMapTypeControlOpts(
            type_=BMapType.MAPTYPE_CONTROL_DROPDOWN
        ),
        scale_control_opts=opts.BMapScaleControlOpts(),
        overview_map_opts=opts.BMapOverviewMapControlOpts(is_open=True),
        navigation_control_opts=opts.BMapNavigationControlOpts(),
        #geo_location_control_opts=opts.BMapGeoLocationControlOpts(),
    )
    .render("out_gomap.html")
)
 
#hotmap.render_notebook()
system('out_gomap.html')