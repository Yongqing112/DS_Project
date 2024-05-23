import pandas as pd
import matplotlib.pyplot as plt
import caculate
import caculate_public_or_private
import caclulate_school_type
from matplotlib.ticker import FuncFormatter

def draw_plot(data, columns, xlabel, ylabel, title):
    for column in columns:
        plt.plot(data["學年度"], data[column])

    ax = plt.gca()
    ax.get_xaxis().set_major_locator(plt.MaxNLocator(integer=True))
    plt.xlabel(xlabel)    # x軸標籤
    plt.ylabel(ylabel)    # y軸標籤
    plt.legend(columns, loc="lower right")    # 圖示，共有左下、左上、右下、右上四個方位
    plt.title(title)    # 主標題
    plt.grid(True)    # 是否有網格?

def draw_all(df, columns):
    data = pd.DataFrame()
    data = caculate.not_higher_education_and_not_get_job(df, data, 106, 110, columns)

    # 繪圖 圖畫在圖1上
    plt.figure(1)
    draw_plot(data, columns, "學年度", "人數", "未升學未就業情形")
    plt.savefig("未升學未就業情形" + ".png")
    plt.show()

def draw_all_not_have_further_studies(df, columns):
    data = pd.DataFrame()
    data = caculate.not_higher_education_and_not_get_job(df, data, 106, 110, columns)

    # 繪圖 圖畫在圖2上
    plt.figure(2)
    draw_plot(data, columns, "學年度", "人數", "未升學未就業情形")
    plt.savefig("未升學未就業情形_去掉補習或準備升學人數" + ".png")
    plt.show()

def draw_public_private(df, columns):
    data = pd.DataFrame()
    data = caculate_public_or_private.not_higher_education_and_not_get_job(df, data, 106, 110, "國立", columns)
    print(data)

    # 繪圖 圖畫在圖3上
    plt.figure(3)
    plt.subplot(1, 2, 1)
    draw_plot(data, columns, "學年度", "人數", "未升學未就業情形_國立",)

    data = pd.DataFrame()
    data = caculate_public_or_private.not_higher_education_and_not_get_job(df, data, 106, 110, "私立", columns)

    # 繪圖 圖畫在圖3上
    plt.figure(3)
    plt.subplot(1, 2, 2)
    draw_plot(data, columns, "學年度", "人數", "未升學未就業情形_私立",)

    plt.savefig("未升學未就業情形_國立_私立_去掉補習或準備升學人數" + ".png")
    plt.show()

def draw_school_type(df, school_type, columns):
    data = pd.DataFrame()
    data = caclulate_school_type.not_higher_education_and_not_get_job(df, data, 106, 110, school_type[0], columns)
    # 繪圖 圖畫在圖4上
    plt.figure(4)
    draw_plot(data, columns, "學年度", "人數", "未升學未就業情形_普通科")
    plt.savefig("未升學未就業情形_普通科" + ".png")
    plt.show()

    data = pd.DataFrame()
    data = caclulate_school_type.not_higher_education_and_not_get_job(df, data, 106, 110, school_type[1], columns)
    # 繪圖 圖畫在圖4上
    plt.figure(4)
    draw_plot(data, columns, "學年度", "人數", "未升學未就業情形_專業群科")
    plt.savefig("未升學未就業情形_專業群科" + ".png")
    plt.show()

    data = pd.DataFrame()
    data = caclulate_school_type.not_higher_education_and_not_get_job(df, data, 106, 110, school_type[2], columns)
    # 繪圖 圖畫在圖4上
    plt.figure(5)
    draw_plot(data, columns, "學年度", "人數", "未升學未就業情形_綜合高中")
    plt.savefig("未升學未就業情形_綜合高中" + ".png")
    plt.show()

    data = pd.DataFrame()
    data = caclulate_school_type.not_higher_education_and_not_get_job(df, data, 106, 110, school_type[3], columns)
    # 繪圖 圖畫在圖4上
    plt.figure(5)
    draw_plot(data, columns, "學年度", "人數", "未升學未就業情形_實用技能學程")
    plt.savefig("未升學未就業情形_實用技能學程" + ".png")
    plt.show()

    data = pd.DataFrame()
    data = caclulate_school_type.not_higher_education_and_not_get_job(df, data, 106, 110, school_type[4], columns)
    # 繪圖 圖畫在圖4上
    plt.figure(6)
    draw_plot(data, columns, "學年度", "人數", "未升學未就業情形_進修部")
    plt.savefig("未升學未就業情形_進修部" + ".png")
    plt.show()

def draw_school_type_percent(df, school_type, people, columns):
    for column in columns:
        data = pd.DataFrame()
        data = caclulate_school_type.not_higher_education_and_not_get_job_percent(df, data, 106, 110, school_type, people, column)
        # 繪圖 圖畫在圖4上
        plt.figure(4)
        fig = plt.get_current_fig_manager()
        fig.window.state('zoomed')
        draw_plot_percent2(data, "學年度", "人數", "各學程的"+ column, column)
        plt.savefig("各學程的" + column + "_比率" + ".png")
        plt.show()

def draw_plot_percent(data, xlabel, ylabel, title, column):
    # print(data.columns)
    pivot_df = data.pivot(index='學年度', columns='學程別', values= column)
    for pcolumn in pivot_df.columns:
        # plt.plot(data["學年度"], data[columns[0]])
        # print(pivot_df.columns)
        plt.plot(pivot_df.index, pivot_df[pcolumn], marker='o', label=pcolumn)

    ax = plt.gca()
    ax.get_xaxis().set_major_locator(plt.MaxNLocator(integer=True))
    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
    plt.xlabel(xlabel)    # x軸標籤
    plt.ylabel(ylabel)    # y軸標籤
    plt.xticks(pivot_df.index)
    plt.legend(pivot_df.columns, loc="lower right")    # 圖示，共有左下、左上、右下、右上四個方位
    plt.title(title)    # 主標題
    plt.grid(True)    # 是否有網格?

def to_percent(y, position):
    return f'{y:.0f}%'

def draw_school_type_percent2(df, school_type, people, columns):
    data = pd.DataFrame()
    for column in columns:
        data = caclulate_school_type.not_higher_education_and_not_get_job_percent2(df, data, 106, 110, school_type, people, column)
    # 繪圖 圖畫在圖4上
    print(data)
    plt.figure(4)
    fig = plt.get_current_fig_manager()
    fig.window.state('zoomed')
    draw_plot_percent2(data, "學年度", "人數", school_type[0], columns)
    plt.savefig(school_type[0] + "_比率" + ".png")
    plt.show()

def draw_plot_percent2(data, xlabel, ylabel, title, column):
    for pcolumn in column:
        plt.plot(data["學年度"], data[pcolumn], marker='o', label=pcolumn)

    ax = plt.gca()
    ax.get_xaxis().set_major_locator(plt.MaxNLocator(integer=True))
    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
    plt.xlabel(xlabel)    # x軸標籤
    plt.ylabel(ylabel)    # y軸標籤
    plt.xticks(data["學年度"])
    plt.legend(column, loc="lower right")    # 圖示，共有左下、左上、右下、右上四個方位
    plt.title(title)    # 主標題
    plt.grid(True)    # 是否有網格?