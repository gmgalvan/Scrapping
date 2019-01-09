import unittest
from selenium_agent import Agent

class TestAgent(unittest.TestCase):
    def setUp(self):
        self.my_agent = Agent(focus_page="https://coinmarketcap.com")
    
    def test_source(self):
        assert "bitcoin" in self.my_agent.source(), "Page not releated to cryptocurrencies."

    def tearDown(self):
        self.my_agent.end()

if __name__ == '__main__':
    unittest.main()