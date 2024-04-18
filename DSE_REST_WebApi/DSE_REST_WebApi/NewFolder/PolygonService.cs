using Microsoft.AspNetCore.Mvc;
using System.Text.Json;
using System.Text.Json.Nodes;

namespace WSE_REST_WebApi.NewFolder
{
    public class PolygonService
    {
        private static readonly string APIKey = "inium9MbgdoGg2YQ23zMkvYggnTWT7DH";
        private static readonly string BaseUrl = "https://api.polygon.io/v2/aggs/";
        public static async Task<ActionResult<Stream>> GetStockHistoryAsync(string symbol)
        {
            using (HttpClient _httpClient = new HttpClient())
            {
                var query = $"{BaseUrl}daily/{symbol}?token={APIKey}";
                var response = await _httpClient.GetAsync(query);
                response.EnsureSuccessStatusCode();
                var stock = await response.Content.ReadAsStreamAsync();
                return stock;
            }
        }

        public static async Task<ActionResult<JsonNode>> GetStockPrevCloseAsync(string symbol)
        {
            using (HttpClient _httpClient = new HttpClient())
            {
                var query = $"{BaseUrl}ticker/{symbol}/prev?adjusted=true&apiKey={APIKey}";
                var response = await _httpClient.GetAsync(query);
                response.EnsureSuccessStatusCode();
                string str = await response.Content.ReadAsStringAsync();
                var stock = JsonNode.Parse(str);
                var root = stock["results"];
                Console.WriteLine(root.ToJsonString());
                return root;
            }
        }
    }
}
