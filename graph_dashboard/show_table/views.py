from django.shortcuts import render
import pandas as pd
from highcharts.


def table_html(request):
    # df = pd.read_csv('data/car_sales.csv')
    # table_data_html = df.to_html(index=None)
    # table_data_html = table_data_html.replace('class="dataframe"', "class='table table-striped'")
    # table_data_html = table_data_html.replace('border="1"', "")
    table_data_html_direct = """
    <table  class='table table-striped table-bordered table-hover table-sm table-dark'>
  <thead>
    <tr style="text-align: right;">
      <th>Manufacturer</th>
      <th>Model</th>
      <th>Sales in thousands</th>
      <th>4-year resale value</th>
      <th>Vehicle type</th>
      <th>Price in thousands</th>
      <th>Engine size</th>
      <th>Horsepower</th>
      <th>Wheelbase</th>
      <th>Width</th>
      <th>Length</th>
      <th>Curb weight</th>
      <th>Fuel capacity</th>
      <th>Fuel efficiency</th>
      <th>Latest Launch</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Acura</td>
      <td>Integra</td>
      <td>16.919</td>
      <td>16.360</td>
      <td>Passenger</td>
      <td>21.5</td>
      <td>1.8</td>
      <td>140</td>
      <td>101.2</td>
      <td>67.3</td>
      <td>172.4</td>
      <td>2.639</td>
      <td>13.2</td>
      <td>28</td>
      <td>2-Feb-14</td>
    </tr>
    <tr>
      <td>Acura</td>
      <td>TL</td>
      <td>39.384</td>
      <td>19.875</td>
      <td>Passenger</td>
      <td>28.4</td>
      <td>3.2</td>
      <td>225</td>
      <td>108.1</td>
      <td>70.3</td>
      <td>192.9</td>
      <td>3.517</td>
      <td>17.2</td>
      <td>25</td>
      <td>6-Mar-15</td>
    </tr>
    <tr>
      <td>Acura</td>
      <td>CL</td>
      <td>14.114</td>
      <td>18.225</td>
      <td>Passenger</td>
      <td>.</td>
      <td>3.2</td>
      <td>225</td>
      <td>106.9</td>
      <td>70.6</td>
      <td>192.0</td>
      <td>3.470</td>
      <td>17.2</td>
      <td>26</td>
      <td>1-Apr-14</td>
    </tr>
    <tr>
      <td>Acura</td>
      <td>RL</td>
      <td>8.588</td>
      <td>29.725</td>
      <td>Passenger</td>
      <td>42</td>
      <td>3.5</td>
      <td>210</td>
      <td>114.6</td>
      <td>71.4</td>
      <td>196.6</td>
      <td>3.850</td>
      <td>18.0</td>
      <td>22</td>
      <td>3-Oct-15</td>
    </tr>
    <tr>
      <td>Audi</td>
      <td>A4</td>
      <td>20.397</td>
      <td>22.255</td>
      <td>Passenger</td>
      <td>23.99</td>
      <td>1.8</td>
      <td>150</td>
      <td>102.6</td>
      <td>68.2</td>
      <td>178.0</td>
      <td>2.998</td>
      <td>16.4</td>
      <td>27</td>
      <td>10-Aug-15</td>
    </tr>
    <tr>
      <td>Audi</td>
      <td>A6</td>
      <td>18.780</td>
      <td>23.555</td>
      <td>Passenger</td>
      <td>33.95</td>
      <td>2.8</td>
      <td>200</td>
      <td>108.7</td>
      <td>76.1</td>
      <td>192.0</td>
      <td>3.561</td>
      <td>18.5</td>
      <td>22</td>
      <td>8-Sep-15</td>
    </tr>
  </tbody>
</table>
    """
    context = {'table_html': table_data_html_direct}
    return render(request, 'table.html', context=context)


# print(table_html(''))

