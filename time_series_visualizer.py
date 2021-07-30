import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'])

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    sns.lineplot(data=df, y='value', x=df.index, ax=ax)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby(pd.PeriodIndex(df.index, freq='M'))['value'].mean().to_frame()
    df_bar.columns = ['Average Page Views']
    df_bar['Years'] = df_bar.index.year
    df_bar['Months'] = df_bar.index.to_timestamp().month_name()

    # Draw bar plot
    graph = sns.catplot(data=df_bar, kind='bar', x='Years', hue='Months', y='Average Page Views')
    fig = graph.fig
    

    plt.legend(labels=('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'), loc='upper left', bbox_to_anchor=(0, 1))

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.columns = ['Page Views']
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)    
    fig, axes = plt.subplots(ncols=2, sharey=True)
    sns.boxplot(ax=axes[0], data=df_box, x='Year', y='Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(ax=axes[1], data=df_box, x='Month', y='Page Views', order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
