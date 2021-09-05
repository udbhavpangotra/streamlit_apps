import pandas as pd
import streamlit as st
import yfinance


@st.cache
def load_data():
    components = pd.read_html('https://en.wikipedia.org/wiki/List_of_S'
                              '%26P_500_companies')[0]
    return components.drop('SEC filings', axis=1).set_index('Symbol')


@st.cache(allow_output_mutation=True)
def load_quotes(asset):
    return yfinance.download(asset)


def main():
    components = load_data()
    title = st.empty()
    st.sidebar.title("Main Menu")
    st.sidebar.text(
        "You can view a list of companies \nas well, use the checkbox to do so.\nThe default stock is Apple")

    def label(symbol):
        a = components.loc[symbol]
        return symbol + ' - ' + a.Security
    st.title('Stock Viewer Dashboard')

    if st.sidebar.checkbox('View companies list'):
        st.write(
            '''Here we have a list of companies that are in S&P and can be viewed over here''')
        st.dataframe(components[['Security',
                                 'GICS Sector',
                                #  'Date first added',
                                 'Founded']], width=2000)

    st.sidebar.subheader('Select asset')
    asset = st.sidebar.selectbox('Click below to select a new asset',
                                 components.index.sort_values(), index=3,
                                 format_func=label)
    # st.text(components.loc[asset])

    st.write('''
             \n
             \n
             ''')
    st.write("\n The stock selected by you is **" +
             components.loc[asset].Security+"**"+"\n. The Plots for the stock you have selected :")
    if st.sidebar.checkbox('View company info', True):
        st.text('''Some information about the selected stock''')
        st.text(components.loc[asset])

    data0 = load_quotes(asset)
    data = data0.copy().dropna()
    data.index.name = None
    # st.dataframe(data)
    section = st.sidebar.slider('Number of quotes', min_value=30,
                                max_value=min([100000, data.shape[0]]),
                                value=round(data.shape[0] / 2),  step=100)

    data2 = data[-section:]['Adj Close'].to_frame('Adj Close')
    sma = st.sidebar.checkbox('SMA')
    if sma:
        period = st.sidebar.slider('SMA period', min_value=5, max_value=500,
                                   value=20,  step=1)
        data[f'SMA {period}'] = data['Adj Close'].rolling(period).mean()
        data2[f'SMA {period}'] = data[f'SMA {period}'].reindex(data2.index)

    sma2 = st.sidebar.checkbox('SMA2')
    if sma2:
        period2 = st.sidebar.slider('SMA2 period', min_value=5, max_value=500,
                                    value=100,  step=1)
        data[f'SMA2 {period2}'] = data['Adj Close'].rolling(period2).mean()
        data2[f'SMA2 {period2}'] = data[f'SMA2 {period2}'].reindex(data2.index)
        # st.table(data2 )
    st.subheader('Plot for the Adjusted Close Value ')
    st.line_chart(data2)
    # st.line_chart(data_2)
    if st.sidebar.checkbox('View statistic'):
        st.subheader('Statistics for the selected stock')
        st.table(data2.describe())

    if st.sidebar.checkbox('View quotes'):
        st.subheader(f'{asset} historical data')
        st.table(data2.head(10))

    st.sidebar.title("About")
    st.sidebar.info('This app is a simple example of '
                    'using Streamlit to create a \n financial data web app.\n'
                    '\nIt is maintained by [Udbhav Pangotra]('
                    'https://www.linkedin.com/in/udbhav-pangotra/).\n\n'
                    'Check the code at ')


if __name__ == '__main__':
    main()
