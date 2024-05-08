namespace WSE_REST_WebApi.NewFolder
{
    public class TiingoService
    {
        //private readonly static HttpClient _httpClient;
        private readonly static string frosToken = "78e2a84e3c3fd84749a6d9b171689dc4a08e8f7b";
        private static readonly string  BaseUrl = "https://api.tiingo.com/tiingo/";

        public static async Task<string> GetStockByTicker(string ticker)
        {
            using (HttpClient _httpClient = new HttpClient())
            {
                var query = $"{BaseUrl}daily/{ticker}?token={frosToken}";
                var response = await _httpClient.GetAsync(query);

                response.EnsureSuccessStatusCode();
                var stock = await response.Content.ReadAsStringAsync();
                                                  //.ReadAsStreamAsync();
                return stock;
                
                //var responsePrice = await _httpClient.GetAsync(query);
                //var price = $"{BaseUrl}daily/{ticker}/prices?startDate={}&token={frosToken}";
                //var queryPrice = https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2019-01-02&token=
            }
        }

        public static async Task<string?> GetStockPrices(string ticker,int timespan)
        {
            using (HttpClient _httpClient = new HttpClient())
            {
                if (timespan >= 730 || timespan < 0) { return null; ; }
                DateTime history = DateTime.Today.AddDays(-timespan);
                var price = $"{BaseUrl}daily/{ticker}/prices?startDate={history.ToString("yyyy-MM-dd")}&token={frosToken}";
                var response = await _httpClient.GetAsync(price);
                
                response.EnsureSuccessStatusCode();
                var stock = await response.Content.ReadAsStringAsync();
                return stock;

                
                //var queryPrice = https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2019-01-02&token=
            }
        }
    }
}
