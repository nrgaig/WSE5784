using WSE_REST_WebApi.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Data.SqlClient.DataClassification;
using System.Net.Http;
using WSE_REST_WebApi.NewFolder;
using Microsoft.CodeAnalysis;
using WSE_REST_WebApi.Convertor;
using System.Linq;
using Microsoft.Extensions.Hosting;
using System.Collections.ObjectModel;
using System.Reflection.Metadata;
using System.Text.Json.Serialization;
using System.Text.Json;
using NuGet.Packaging;
using static Microsoft.EntityFrameworkCore.DbLoggerCategory;

namespace WSE_REST_WebApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class StockController : ControllerBase
    {
        private readonly StockContext _dbContext;
        private readonly HttpClient _httpClient;
        private readonly string frosToken = "78e2a84e3c3fd84749a6d9b171689dc4a08e8f7b";
        public StockController(StockContext dbContext)
        {
            _dbContext = dbContext;
            _httpClient = new HttpClient();
        }
        private readonly StockContext API_dbContext;


        //GET: api/Stocks
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Stock>>> GetAllStocks()
        {
            if (_dbContext.Stocks == null) { return NotFound(); }

            return await _dbContext.Stocks.ToListAsync();
        }

        [HttpGet("stocks")]
        public async Task<ActionResult<IEnumerable<Stock>>> GetStocksWithPrices(int stockId)
        {
            // Retrieve stocks from the database including TiingoPriceDtos
           //var a= _dbContext.TiingoPriceDtos.Where(t => t.StockId == stockId).ToList();

            var stocks = await _dbContext.GetTiingoPricesFromStockId(stockId);
            //var s = await GetStockId(stockId);
            Stock s= await _dbContext.Stocks.FindAsync(stockId);
            s.TiingoPriceDtos = stocks;

            var options = new JsonSerializerOptions
            {
                ReferenceHandler = ReferenceHandler.Preserve,
                // Other options if needed
            };

            // Serialize the Stock object to JSON with circular references
            var json = JsonSerializer.Serialize(s, options);

            // Return the JSON string as ContentResult
            return Content(json, "application/json");
            return Ok(s);
        }

        [HttpGet("stocks/{input}")]
        public async Task<ActionResult<IEnumerable<Stock>>> GetStocksWithPricesByString(string input)
        {
            // Retrieve stocks from the database including TiingoPriceDtos
            //var a= _dbContext.TiingoPriceDtos.Where(t => t.StockId == stockId).ToList();
            var stock = await _dbContext.Stocks.FirstOrDefaultAsync(s => s.Name == input || s.Ticker == input);
            var stockPrice = await _dbContext.GetTiingoPricesFromStockId(stock.Id);
            //var s = await GetStockId(stockId);
            stock.TiingoPriceDtos = stockPrice;

            var options = new JsonSerializerOptions
            {
                ReferenceHandler = ReferenceHandler.Preserve,
                // Other options if needed
            };

            // Serialize the Stock object to JSON with circular references
            var json = JsonSerializer.Serialize(stock, options);

            // Return the JSON string as ContentResult
            return Content(json, "application/json");
            return Ok(stock);
        }

        //GET: api/Stock/tiingo/NVDA
        [HttpGet("tiingo/{symbol}")]
        public async Task<ActionResult<Stock?>> TiingoGetStockIdAsync(string symbol)
        {
           
                var stock = await TiingoService.GetStockByTicker(symbol);
                if (stock == null) {
                    Console.WriteLine("1");
                    return NotFound(); 
                }

                return await stockFromJsons(symbol, 1);
           
                // Handle exceptions
                Console.WriteLine("2");

                return NotFound();
            
        }

        //GET: api/Stock/tiingo/NVDA/graph/30
        [HttpGet("tiingo/{symbol}/graph/{from}")]
        public async Task<ActionResult<Stock?>> TiingoGetStockPriceAsync(string symbol, int from)
        {
            
                var stock = await TiingoService.GetStockPrices(symbol, from);
                if (stock == null) {
                    Console.WriteLine("3");

                    return NotFound(); }
                return await stockFromJsons(symbol, from);
            
            
                Console.WriteLine("4");

                // Handle exceptions
                return NotFound();
            
        }

        //GET: api/Stock/polygon/NVDA/graph/30
        [HttpGet("polygon/{symbol}/graph/{from}")]
        public async Task<ActionResult<Stream>> GetStockPrevCloseAsync(string symbol, int from)
        {
           
                var stock = await PolygonService.GetStockHistoryAsync(symbol,from);
                if (stock == null) { return NotFound(); }
                return Ok(stock);
            
            
                // Handle exceptions
                return NotFound();
            
        }

        //GET: api/Stock/polygon/prev/NVDA
        [HttpGet("polygon/prev/{symbol}")]
        public async Task<ActionResult<string>> GetStockPrevCloseAsync(string symbol)
        {
            
                var stock = await PolygonService.GetStockPrevCloseAsync(symbol);
                if (stock == null) { return NotFound(); }
                return Ok(stock.Value.ToJsonString());
                //return stock;
            
            
                // Handle exceptions
                return NotFound();
           
        }

        //GET: api/Stock/5
        [HttpGet("{stockId}")]
        public async Task<ActionResult<Stock>> GetStockId(int stockId)
        {
            if (_dbContext.Stocks == null) { return NotFound(); }


            var stocks = await _dbContext.GetTiingoPricesFromStockId(stockId);
            //var s = await GetStockId(stockId);
            Stock s = await _dbContext.Stocks.FindAsync(stockId);
            s.TiingoPriceDtos = stocks;

            //var stock = await _dbContext.Stocks.FindAsync(id);
            if (s == null) { return NotFound(); }
            var prices= await _dbContext.GetTiingoPricesFromStockId(stockId);
            s.TiingoPriceDtos = prices;

            var options = new JsonSerializerOptions
            {
                ReferenceHandler = ReferenceHandler.Preserve,
                // Other options if needed
            };

            // Serialize the Stock object to JSON with circular references
            var json = JsonSerializer.Serialize(s, options);

            // Return the JSON string as ContentResult
            return Content(json, "application/json");

            return Ok(s);
        }

        //GET: /api/Stock/s/APPL
        [HttpGet("s+dayprice/{ticker}")]
        public async Task<ActionResult<Stock>> GetStockDailyByTicker(string ticker)
        {
            if (_dbContext.Stocks == null) { return NotFound(); }

            var stock = await _dbContext.Stocks.FirstOrDefaultAsync(s => s.Ticker == ticker);
            if (stock == null) { return NotFound(); }
            var con = new JsonConverotr();
            var stockPrice = await TiingoService.GetStockPrices(ticker, 1);
            var TiingoPriceDtos = new List<TiingoPriceDto>(con.GetStockObjFromJson(stockPrice));
            stock.Value = TiingoPriceDtos.FirstOrDefault().close;
            //stock.Open = TiingoPriceDtos.FirstOrDefault().open;

            return Ok(stock);
        }


        //GET: /api/Stock/s/APPL
        [HttpGet("s/{input}")]
        public async Task<ActionResult<Stock>> GetStockNameSymbol(string input)
        {
            if (_dbContext.Stocks == null) { return NotFound(); }

            var stock = await _dbContext.Stocks.FirstOrDefaultAsync(s => s.Name == input||s.Ticker==input);
            if (stock == null) { return NotFound(); }
            return Ok(stock);
        }

        //GET: /api/Stock/q/APPL
        [HttpGet("q/{query}")]
        public async Task<ActionResult<IEnumerable<Stock>>> GetStockByQuery(string query)
        {
            if (_dbContext.Stocks == null) { return NotFound(); }

            var stocks = await _dbContext.Stocks
                .Where(s => s.Name.Contains(query) || s.Ticker.Contains(query))
                .ToListAsync();

            if (!stocks.Any()) { return NotFound(); }

            return Ok(stocks);
        }

        //GET: /api/Stock/q/APPL
        [HttpGet("StockDescription/{query}")]
        public async Task<ActionResult<string>> GetOneStockDescription(string query)
        {
            if (_dbContext.Stocks == null) { return NotFound(); }

            var stock = await _dbContext.Stocks
                .Where(s => s.Name.Contains(query) || s.Ticker.Contains(query))
                .FirstOrDefaultAsync();

            if (stock == null) { return NotFound(); }

            return Ok(stock.Description);
        }


        ////GET: /api/Stock/q/APPL/30
        //[HttpGet("DataBase/{ticker}/db/{days}")]
        //public async Task<ActionResult<IEnumerable<TiingoPriceDto>>> GetTiingPriceListDatabase(string ticker)
        //{
        //    //var stockPrice = await TiingoService.GetStockPrices(ticker, days);
        //    //
        //    //stock.EconomicDescription = new List<TiingoPriceDto>(con.GetStockObjFromJson(stockPrice));
        //    //var lastElement = stock.EconomicDescription?.LastOrDefault();
        //    var stock = await _dbContext.Stocks.FirstOrDefaultAsync(s => s.Ticker == ticker);
        //    int stockId = stock.Id;
        //    var prices = await _dbContext.GetTiingoPricesFromStockId(stockId);
        //    var con = new JsonConverotr();
        //    var EconomicDescription = new List<TiingoPriceDto>(con.GetStockObjFromJson(prices));
        //    return EconomicDescription;

        //}

        //GET: /api/Stock/q/APPL/30
        [HttpGet("TiingoPriceDtoList/{ticker}/db/{days}")]
        public async Task<ActionResult<IEnumerable<TiingoPriceDto>>> GetTiingPriceList(string ticker,int days)
        {
            var stockPrice = await TiingoService.GetStockPrices(ticker, days);
            //
            //stock.EconomicDescription = new List<TiingoPriceDto>(con.GetStockObjFromJson(stockPrice));
            //var lastElement = stock.EconomicDescription?.LastOrDefault();
            var con = new JsonConverotr();
            var EconomicDescription = new List<TiingoPriceDto>(con.GetStockObjFromJson(stockPrice));
            return EconomicDescription;

        }



        // POST: api/Stocks/
        [HttpPost("tiingoPost/{ticker}/db/{days}")]
        public async Task<ActionResult<Stock>> PostStock(string ticker, int days)
        {
            //var existStock = await _dbContext.Stocks.FirstOrDefaultAsync(s => s.Ticker == ticker);
            //if (existStock != null) { return Ok(existStock); }
            //לבדוק אם זה באמת הערך שצריך להחזיר

            var stock = new Stock();

            var stockQ = await TiingoService.GetStockByTicker(ticker);
            if (stockQ == null) { return null; }
            var con = new JsonConverotr();
            stock = con.GetStockFromJson(stockQ);
            stock.TiingoPriceDtos = new Collection<TiingoPriceDto>();
            var stockPrice = await TiingoService.GetStockPrices(ticker, days);
            //
            //stock.EconomicDescription = new List<TiingoPriceDto>(con.GetStockObjFromJson(stockPrice));
            //var lastElement = stock.EconomicDescription?.LastOrDefault();
            
            var EconomicDescription = new List<TiingoPriceDto>(con.GetStockObjFromJson(stockPrice));
            stock.TiingoPriceDtos.AddRange(EconomicDescription);
            var lastElement = EconomicDescription.LastOrDefault();
            if (lastElement != null)
            {
                stock.Value = lastElement.close;
                //stock.Open = lastElement.open;
            }
            //stock.Value = lastElement.close;
            _dbContext.Stocks.Add(stock);

            await _dbContext.SaveChangesAsync();

            // Configure JsonSerializerOptions to support cycles
            var options = new JsonSerializerOptions
            {
                ReferenceHandler = ReferenceHandler.Preserve,
                // Other options if needed
            };

            // Serialize the Stock object to JSON with circular references
            var json = JsonSerializer.Serialize(stock, options);

            // Return the JSON string as ContentResult
            return Content(json, "application/json");
            //return stock;

        }




        ////POST: 
        //[HttpPost]
        //public async Task<ActionResult<Stock>> PostStock(Stock stock)
        //{
        //    _dbContext.Stocks.Add(stock);
        //    await _dbContext.SaveChangesAsync();
        //    return Ok(CreatedAtAction(nameof(PostStock), new { id = stock.Id }, stock));
        //}

        //PUT:
        [HttpPut("{id}")]
        public async Task<IActionResult> PutStock(int id,Stock stock)
        {
            if (id!=stock.Id)   
            {
                return BadRequest();
            }
            _dbContext.Entry(stock).State = EntityState.Modified;

            try
            {
                await _dbContext.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!StockExists(id))
                {
                    return NotFound();
                }
                else { throw; }
            }
            return NoContent();
        }
        private bool StockExists(int id)
        {
            return (_dbContext.Stocks?.Any(e => e.Id == id)).GetValueOrDefault();
        }

        //DELETE:
        [HttpDelete("{id}")]
        public async Task<IActionResult>DeleteStock(int id)
        {
            if (_dbContext.Stocks == null) { return NotFound(); }

            var stock = await _dbContext.Stocks.FindAsync(id);
            if (stock == null) { return NotFound(); }

            _dbContext.Stocks.Remove(stock);
            await _dbContext.SaveChangesAsync();

            return NoContent();

        }

   



        //GET: api/Stock/tiingo/NVDA/many/30
        [HttpGet("tiingo/{ticker}/many/{days}")]
        public async Task<ActionResult<Stock?>> stockFromJsons(string ticker, int days)
        {
            var stock = new Stock();
            var stockQ = await TiingoService.GetStockByTicker(ticker);
            if (stockQ == null) { return null; }
            var con = new JsonConverotr();
            stock = con.GetStockFromJson(stockQ);
            var stockPrice = await TiingoService.GetStockPrices(ticker, days);
            stock.TiingoPriceDtos = new List<TiingoPriceDto>(con.GetStockObjFromJson(stockPrice));
            //var lastElement = stock.EconomicDescription?.LastOrDefault();

            //stock.Value = lastElement.close;
            //stock.EconomicDescriptionJson = await TiingoService.GetStockIdPrice(ticker, days);
            return stock;
        }
    }
}
