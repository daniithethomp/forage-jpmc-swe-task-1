import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    self.assertEqual(getDataPoint(quotes[0])[3], (120.48+121.2)/2)
    self.assertEqual(getDataPoint(quotes[1])[3], (121.68+117.87)/2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    self.assertEqual(getDataPoint(quotes[0])[3], (119.2+120.48)/2)
    self.assertEqual(getDataPoint(quotes[1])[3], (121.68+117.87)/2)

  def test_getDataPoint_calculatePriceBidLessThanAsk(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.172497214091', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    self.assertEqual(getDataPoint(quotes[0])[3], (121.2+120.48)/2)
    self.assertEqual(getDataPoint(quotes[1])[3], (121.68+117.87)/2)

  def test_getDataPoint_calculatePriceBidZero(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.172497214091', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    self.assertEqual(getDataPoint(quotes[0])[3], 121.2/2)
    self.assertEqual(getDataPoint(quotes[1])[3], 121.68/2)
  
  def test_getRatio_calculateRatio(self):
    self.assertEqual(getRatio(10, 5), 2)
    self.assertEqual(getRatio(5, 10), 0.5)

  def test_getRatio_calculateRatioPriceBZero(self):
    self.assertEqual(getRatio(5, 0), 0)

  def test_getRatio_calculateRatioPriceAZero(self):
    self.assertEqual(getRatio(0, 5), 0)

  def test_getRatio_calculateRatioBothZero(self):
    self.assertEqual(getRatio(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
