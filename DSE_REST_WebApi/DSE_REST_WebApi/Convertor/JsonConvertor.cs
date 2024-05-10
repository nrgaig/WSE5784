using Newtonsoft.Json;
using WSE_REST_WebApi.Models;

namespace WSE_REST_WebApi.Convertor
{
    public class JsonConverotr
    {
        

        public IEnumerable<TiingoPriceDto> GetStockObjFromJson(string json)
        {
            var searchResults = JsonConvert.DeserializeObject<List<TiingoPrice>>(json);

            // Convert each TiingoPrice object to TiingoPriceDto
            return searchResults?.Select(res => convertTiingoPriceToTiingoPriceDto(res));
        }
        private static TiingoPriceDto convertTiingoPriceToTiingoPriceDto(TiingoPrice res)
        {
            // parsing the year for movie
            if (!double.TryParse(res.close, out double close))
            {
                close = 0;
            }
            if (!double.TryParse(res.high, out double high))
            {
                high = 0;
            }
            if (!double.TryParse(res.low, out double low))
            {
                low = 0;
            }
            if (!double.TryParse(res.open, out double open))
            {
                open = 0;
            }
            if (!double.TryParse(res.volume, out double volume))
            {
                volume = 0;
            }

            if (!double.TryParse(res.divCash, out double divCash))
            {
                divCash = 0;
            }
            if (!double.TryParse(res.splitFactor, out double splitFactor))
            {
                splitFactor = 0;
            }
            return new TiingoPriceDto
            {
                date = res.date,
                close = close,
                high = high,
                low = low,
                open = open,
                volume = volume,
                divCash = divCash,
                splitFactor = splitFactor
            };
        }


        public Stock? GetStockFromJson(string json)
        {
            return JsonStockDeserialization.GetStockResult(json);
        }

        internal class SearchResponse
        {
            public List<TiingoPrice>? Search { get; set; }
            public string? TotalResult { get; set; }
            public bool Response { get; set; }
        }

        internal class TiingoQuery
        {
            public string? ticker { get; set; }
            public string? name { get; set; }
            public string? description { get; set; }
            public string? startDate { get; set; }
            public string? endDate { get; set; }
            public string? exchngeCode { get; set; }
        }

        internal class TiingoPrice
        {
            public string? date { get; set; }
            public string? close { get; set; }
            public string? high { get; set; }
            public string? low { get; set; }
            public string? open { get; set; }
            public string? volume { get; set; }
            public string? adjClose { get; set; }
            public string? adjHigh { get; set; }
            public string? adjLow { get; set; }
            public string? adjOpen { get; set; }
            public string? adjVolume { get; set; }
            public string? divCash { get; set; }
            public string? splitFactor { get; set; }
        }

        internal static class JsonStockDeserialization
        {
            public static IEnumerable<TiingoPriceDto>? GetSearchResults(string json)
            {
                var searchResult = JsonConvert.DeserializeObject<SearchResponse>(json);

                //no data return empty list
                if (searchResult?.Search == null)
                {
                    return new List<TiingoPriceDto> { };
                }

                return (
                from res in searchResult?.Search
                select convertTiingoPriceToTiingoPriceDto(res)
                ).ToList();
            }

      

            public static Stock? GetStockResult(string json)
            {
                var result = JsonConvert.DeserializeObject<TiingoQuery?>(json);
                if (result == null || result.ticker == null || result.name == null)
                {
                    return null;
                }

                return new Stock
                {
                    Name = result.name,
                    Ticker = result.ticker,
                    Description = result.description
                };
            }

        }




    }
}

//using Newtonsoft.Json;
//using System.Collections.Generic;
//using System.Linq;
//using WSE_REST_WebApi.Models;

//namespace WSE_REST_WebApi.Convertor
//{
//    public class JsonConverotr
//    {
//        public IEnumerable<TiingoPriceDto> GetStockObjFromJson(string json)
//        {
//            var searchResults = JsonConvert.DeserializeObject<List<TiingoPrice>>(json);

//            // Convert each TiingoPrice object to TiingoPriceDto
//            return searchResults?.Select(res => convertTiingoPriceToTiingoPriceDto(res));
//        }

//        public Stock? GetStockFromJson(string json)
//        {
//            return JsonStockDeserialization.GetStockResult(json);
//        }

//        private TiingoPriceDto convertTiingoPriceToTiingoPriceDto(TiingoPrice res)
//        {
//            // parsing the year for movie
//            if (!double.TryParse(res.close, out double close))
//            {
//                close = 0;
//            }
//            if (!double.TryParse(res.high, out double high))
//            {
//                high = 0;
//            }
//            if (!double.TryParse(res.low, out double low))
//            {
//                low = 0;
//            }
//            if (!double.TryParse(res.open, out double open))
//            {
//                open = 0;
//            }
//            if (!double.TryParse(res.volume, out double volume))
//            {
//                volume = 0;
//            }

//            if (!double.TryParse(res.divCash, out double divCash))
//            {
//                divCash = 0;
//            }
//            if (!double.TryParse(res.splitFactor, out double splitFactor))
//            {
//                splitFactor = 0;
//            }
//            return new TiingoPriceDto
//            {
//                date = res.date,
//                close = close,
//                high = high,
//                low = low,
//                open = open,
//                volume = volume,
//                divCash = divCash,
//                splitFactor = splitFactor
//            };
//        }

//        internal class SearchResponse
//        {
//            public List<TiingoPrice>? Search { get; set; }
//            public string? TotalResult { get; set; }
//            public bool Response { get; set; }
//        }

//        internal class TiingoQuery
//        {
//            public string? ticker { get; set; }
//            public string? name { get; set; }
//            public string? description { get; set; }
//            public string? startDate { get; set; }
//            public string? endDate { get; set; }
//            public string? exchngeCode { get; set; }
//        }

//        internal class TiingoPrice
//        {
//            public string? date { get; set; }
//            public string? close { get; set; }
//            public string? high { get; set; }
//            public string? low { get; set; }
//            public string? open { get; set; }
//            public string? volume { get; set; }
//            public string? adjClose { get; set; }
//            public string? adjHigh { get; set; }
//            public string? adjLow { get; set; }
//            public string? adjOpen { get; set; }
//            public string? adjVolume { get; set; }
//            public string? divCash { get; set; }
//            public string? splitFactor { get; set; }
//        }

//        internal static class JsonStockDeserialization
//        {
//            public static IEnumerable<TiingoPriceDto>? GetSearchResults(string json)
//            {
//                var searchResult = JsonConvert.DeserializeObject<SearchResponse>(json);

//                //no data return empty list
//                if (searchResult?.Search == null)
//                {
//                    return new List<TiingoPriceDto> { };
//                }

//                return (
//                from res in searchResult?.Search
//                select convertTiingoPriceToTiingoPriceDto(res)
//                ).ToList();
//            }

//            public static Stock? GetStockResult(string json)
//            {
//                var result = JsonConvert.DeserializeObject<TiingoQuery?>(json);
//                if (result == null || result.ticker == null || result.name == null)
//                {
//                    return null;
//                }

//                return new Stock
//                {
//                    Name = result.name,
//                    Ticker = result.ticker,
//                    Description = result.description
//                };
//            }

//        }
//    }
//}



