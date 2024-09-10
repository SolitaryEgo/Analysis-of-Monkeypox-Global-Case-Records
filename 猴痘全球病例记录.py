import pandas as pd
from pyecharts.charts import Line, Bar
import pyecharts.options as opts

df = pd.read_csv('./monkeypox.csv')
print(df.head())
print(df.isna().sum())
print(df.info())
print(df.describe(include='all'))
print(df.shape)

print(df['location'].unique())
print(df['iso_code'].unique())

# 提取芬兰的数据
finland_data = df[df['location'] == 'Finland']

# 提取日期和新增病例
finland_dates = finland_data['date'].tolist()
finland_new_cases = finland_data['new_cases'].tolist()

line = (
    Line()
    .add_xaxis(finland_dates)  # 添加x轴（芬兰的日期）
    .add_yaxis("Finland New Cases", finland_new_cases, is_smooth=True,
               label_opts=opts.LabelOpts(is_show=True))  # 添加y轴（芬兰新增病例）
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Finland Daily New Cases"),
        xaxis_opts=opts.AxisOpts(name="Date"),
        yaxis_opts=opts.AxisOpts(name="New Cases"),
        toolbox_opts=opts.ToolboxOpts()
    )

)

line.render("finland new cases.html")

finland_total_cases = finland_data['total_cases'].tolist()

line2 = (
    Line()
    .add_xaxis(finland_dates)
    .add_yaxis("Finland Total Cases", finland_total_cases, is_smooth=True,
               label_opts=opts.LabelOpts(is_show=True))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Finland Cumulative Cases"),
        xaxis_opts=opts.AxisOpts(name="Date"),
        yaxis_opts=opts.AxisOpts(name="Total Cases"),
        toolbox_opts=opts.ToolboxOpts()
    )
)

line2.render("finland total cases.html")

finland_new_cases_per_million = finland_data['new_cases_per_million'].tolist()

line_per_million = (
    Line()
    .add_xaxis(finland_dates)
    .add_yaxis("Finland New Cases per Million", finland_new_cases_per_million, is_smooth=True,
               label_opts=opts.LabelOpts(is_show=True))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Finland New Cases per Million"),
        xaxis_opts=opts.AxisOpts(name="Date"),
        yaxis_opts=opts.AxisOpts(name="New Cases per Million"),
        toolbox_opts=opts.ToolboxOpts()
    )
)

line_per_million.render("finland new cases per million.html")

world_data = df[df['location'] == 'World']

# 提取日期和总病例、总死亡人数
dates = world_data['date'].tolist()
total_cases = world_data['total_cases'].tolist()
total_deaths = world_data['total_deaths'].tolist()

line_total = (
    Line()
    .add_xaxis(dates)
    .add_yaxis("Total Cases", total_cases, is_smooth=True, label_opts=opts.LabelOpts(is_show=True))
    .add_yaxis("Total Deaths", total_deaths, is_smooth=True, label_opts=opts.LabelOpts(is_show=True))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Global Total Cases and Deaths Over Time"),
        xaxis_opts=opts.AxisOpts(name="Date"),
        yaxis_opts=opts.AxisOpts(name="Count"),
        toolbox_opts=opts.ToolboxOpts(),
    )
)

line_total.render("global_total_cases_and_deaths.html")

# 提取每百万人的总病例和总死亡人数
total_cases_per_million = world_data['total_cases_per_million'].tolist()
total_deaths_per_million = world_data['total_deaths_per_million'].tolist()

line_per_million = (
    Line()
    .add_xaxis(dates)
    .add_yaxis("Total Cases per Million", total_cases_per_million, is_smooth=True,
               label_opts=opts.LabelOpts(is_show=True))
    .add_yaxis("Total Deaths per Million", total_deaths_per_million, is_smooth=True,
               label_opts=opts.LabelOpts(is_show=True))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Global Total Cases and Deaths per Million Over Time"),
        xaxis_opts=opts.AxisOpts(name="Date"),
        yaxis_opts=opts.AxisOpts(name="Count per Million"),
        toolbox_opts=opts.ToolboxOpts(),
    )
)

# 渲染图表
line_per_million.render("global_total_cases_and_deaths_per_million.html")


