using WSE_REST_WebApi.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Data.SqlClient.DataClassification;
using System.Net.Http;
using WSE_REST_WebApi.NewFolder;
using Microsoft.CodeAnalysis;
using WSE_REST_WebApi.Convertor;

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
        public async Task<ActionResult<IEnumerable<Stock>>> GetStocks()
        {
            if (_dbContext.Stocks == null) { return NotFound(); }

            return await _dbContext.Stocks.ToListAsync();
        }

        //GET: api/Stock/tiingo/NVDA
        [HttpGet("tiingo/{symbol}")]
        public async Task<ActionResult<Stock?>> TiingoGetStockIdAsync(string symbol)
        {
            try
            {
                var stock = await TiingoService.GetStockId(symbol);
                if (stock == null) {
                    Console.WriteLine("1");
                    return NotFound(); 
                }

                return await stockFromJsons(symbol, 1);
            }
            catch (Exception ex)
            {
                // Handle exceptions
                Console.WriteLine("2");

                return NotFound();
            }
        }

        //GET: api/Stock/tiingo/NVDA/graph/30
        [HttpGet("tiingo/{symbol}/graph/{from}")]
        public async Task<ActionResult<Stock?>> TiingoGetStockPriceAsync(string symbol, int from)
        {
            try
            {
                var stock = await TiingoService.GetStockIdPrice(symbol, from);
                if (stock == null) {
                    Console.WriteLine("3");

                    return NotFound(); }
                return await stockFromJsons(symbol, from);
            }
            catch (Exception ex)
            {
                Console.WriteLine("4");

                // Handle exceptions
                return NotFound();
            }
        }

        //GET: api/Stock/polygon/NVDA/graph/30
        [HttpGet("polygon/{symbol}/graph/{from}")]
        public async Task<ActionResult<Stream>> GetStockPrevCloseAsync(string symbol, int from)
        {
            try
            {
                var stock = await PolygonService.GetStockHistoryAsync(symbol,from);
                if (stock == null) { return NotFound(); }
                return Ok(stock);
            }
            catch (Exception ex)
            {
                // Handle exceptions
                return NotFound();
            }
        }

        //GET: api/Stock/polygon/prev/NVDA
        [HttpGet("polygon/prev/{symbol}")]
        public async Task<ActionResult<string>> GetStockPrevCloseAsync(string symbol)
        {
            try
            {
                var stock = await PolygonService.GetStockPrevCloseAsync(symbol);
                if (stock == null) { return NotFound(); }
                return Ok(stock.Value.ToJsonString());
                //return stock;
            }
            catch (Exception ex)
            {
                // Handle exceptions
                return NotFound();
            }
        }

        //GET: api/Stock/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Stock>> GetStockId(int id)
        {
            if (_dbContext.Stocks == null) { return NotFound(); }

            var stock = await _dbContext.Stocks.FindAsync(id);
            if (stock == null) { return NotFound(); }
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

        //// GET: /api/Stock/AboveValue/{value}
        //[HttpGet("AboveValue/{value}")]
        //public async Task<ActionResult<IEnumerable<Stock>>> GetStocksAboveValue(double value)
        //{
        //    if (_dbContext.Stocks == null) { return NotFound(); }

        //    var stocks = await _dbContext.Stocks
        //        .Where(s => s.Value > value)
        //        .ToListAsync();

        //    if (!stocks.Any()) { return NotFound(); }

        //    return stocks;
        //}

        //// GET: /api/Stock/BelowValue/{value}
        //[HttpGet("BelowValue/{value}")]
        //public async Task<ActionResult<IEnumerable<Stock>>> GetStocksBelowValue(double value)
        //{
        //    if (_dbContext.Stocks == null) { return NotFound(); }

        //    var stocks = await _dbContext.Stocks
        //        .Where(s => s.Value < value)
        //        .ToListAsync();

        //    if (!stocks.Any()) { return NotFound(); }

        //    return stocks;
        //}





        // POST: api/Stocks/
        [HttpPost("tiingoPost/{ticker}/db/{days}")]
        public async Task<ActionResult<Stock>> PostStock(string ticker, int days)
        {
            var existStock = await _dbContext.Stocks.FirstOrDefaultAsync(s => s.Ticker == ticker);
            if (existStock != null) { return Ok(existStock); }
            //לבדוק אם זה באמת הערך שצריך להחזיר


            var stock = new Stock();
            var stockQ = await TiingoService.GetStockId(ticker);
            if (stockQ == null) { return null; }
            var con = new JsonConverotr();
            stock = con.GetStockFromJson(stockQ);
            var stockPrice = await TiingoService.GetStockIdPrice(ticker, days);
            stock.EconomicDescription = new List<TiingoPriceDto>(con.GetStockObjFromJson(stockPrice));

            _dbContext.Stocks.Add(stock);
            await _dbContext.SaveChangesAsync();
            return stock;

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

        ////shtut
        //[HttpGet("search")]
        //public async Task<ActionResult<string>> Shtut(int x,int y)
        //{
        //    return Ok($"shtut about {x} and {y}\n");
        //}


        //GET: api/Stock/tiingo/NVDA/many/30
        [HttpGet("tiingo/{ticker}/many/{days}")]
        public async Task<ActionResult<Stock?>> stockFromJsons(string ticker, int days)
        {
            var stock = new Stock();
            var stockQ = await TiingoService.GetStockId(ticker);
            if (stockQ == null) { return null; }
            var con = new JsonConverotr();
            stock = con.GetStockFromJson(stockQ);
            var stockPrice = await TiingoService.GetStockIdPrice(ticker, days);
            stock.EconomicDescription = new List<TiingoPriceDto>(con.GetStockObjFromJson(stockPrice));
            return stock;
        }
    }
}
