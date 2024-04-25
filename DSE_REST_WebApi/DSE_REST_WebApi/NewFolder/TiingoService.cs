using Microsoft.AspNetCore.Mvc;
using System;

namespace WSE_REST_WebApi.NewFolder
{
    public class TiingoService
    {
        //private readonly static HttpClient _httpClient;
        private readonly static string frosToken = "78e2a84e3c3fd84749a6d9b171689dc4a08e8f7b";
        private static readonly string  BaseUrl = "https://api.tiingo.com/tiingo/";

        public static async Task<ActionResult<Stream>> GetStockId(string id)
        {
            using (HttpClient _httpClient = new HttpClient())
            {
                var query = $"{BaseUrl}daily/{id}?token={frosToken}";
                var response = await _httpClient.GetAsync(query);
                response.EnsureSuccessStatusCode();
                var stock = await response.Content.ReadAsStreamAsync();
                return stock;
            }
        }
    }
}
