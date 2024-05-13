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
using WSE_REST_WebApi.DAL.Interfaces;
using WSE_REST_WebApi.DAL.Implemantations;

namespace WSE_REST_WebApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class StockController : ControllerBase
    {
        private readonly StockContext _dbContext;
        private readonly HttpClient _httpClient;
        private readonly string frosToken = "78e2a84e3c3fd84749a6d9b171689dc4a08e8f7b";
        private readonly InterfaceReadFromDataBase _readDataBase;
        private readonly InterfaceWriteToDatabase _writeDataBase;


        public StockController(StockContext dbContext)
        {
            _dbContext = dbContext;
            _httpClient = new HttpClient();
            _readDataBase = new ReadFromDataBase(_dbContext);
            // _writeDataBase = new WriteToDatabase(_dbContext);

        }
        private readonly StockContext API_dbContext;

        //all stocks in our database
        //GET: api/Stocks
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Stock>>> GetAllStocks()
        {
            if (_dbContext.Stocks == null) { return NotFound(); }

            //return await _dbContext.Stocks.ToListAsync();
            var stocks = await _readDataBase.GetStocksAsync();
            return Ok(stocks);
        }

        //stock that same with the stockID in  our database
        [HttpGet("stocks")]
        public async Task<ActionResult<IEnumerable<Stock>>> GetStocksWithPrices(int stockId)
        {
            var stockPrice = await _readDataBase.GetPricesByIdAsync(stockId);
            Stock s = await _readDataBase.GetStockByIdAsync(stockId);
            s.TiingoPriceDtos = stockPrice;

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

        //from our database or the fuul ticker or part of the name
        [HttpGet("stocks/{input}")]
        public async Task<ActionResult<IEnumerable<Stock>>> GetStocksWithPricesByString(string input)
        {
            // Retrieve stocks from the database including TiingoPriceDtos
            
            var stock = await _readDataBase.GetStockByTiingoStringAsync(input);
            if (stock == null) { return NotFound(); }  
            var stockPrice = await  _readDataBase.GetPricesByIdAsync(stock.Id);
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

        //Tiingo service 
        //GET: api/Stock/tiingo/NVDA
        [HttpGet("tiingo/{symbol}")]
        public async Task<ActionResult<Stock?>> TiingoGetStockIdAsync(string symbol)
        {

            var stock = await TiingoService.GetStockByTicker(symbol);
            if (stock == null)
            {
                return NotFound();
            }

            return await stockFromJsons(symbol, 1);

            // Handle exceptions

            return NotFound();

        }

        //Tiingo Service
        //GET: api/Stock/tiingo/NVDA/graph/30
        [HttpGet("tiingo/{symbol}/graph/{from}")]
        public async Task<ActionResult<Stock?>> TiingoGetStockPriceAsync(string symbol, int from)
        {

            var stock = await TiingoService.GetStockPrices(symbol, from);
            if (stock == null)
            {

                return NotFound();
            }
            return await stockFromJsons(symbol, from);

            // Handle exceptions
            return NotFound();

        }

       
        //get from our database by stockId
        //GET: api/Stock/5
        [HttpGet("{stockId}")]
        public async Task<ActionResult<Stock>> GetStockId(int stockId)
        {
            if (_dbContext.Stocks == null) { return NotFound(); }
            Stock s = await _readDataBase.GetStockByIdAsync(stockId);
            if (s == null) { return NotFound(); }
            var stockPrice = await _readDataBase.GetPricesByIdAsync(stockId);
            s.TiingoPriceDtos = stockPrice;

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


        //from our database ticker that same to the input string 
        //GET: /api/Stock/s/APPL
        [HttpGet("stockDto/{ticker}")]
        public async Task<ActionResult<StockDto>> GetStockDtoByTicker(string ticker)
        {
            Stock s = await _readDataBase.GetStockByTickerAsync(ticker);
            if (s == null)
            {
                return NotFound();
            }
            var stockPrice = await TiingoService.GetStockPrices(ticker, 5);
            var con = new JsonConverotr();
            var EconomicDescription = new List<TiingoPriceDto>(con.GetStockObjFromJson(stockPrice)).Last();
         

            StockDto stockDto = new StockDto();
            stockDto.Ticker = s.Ticker;
            stockDto.Name = s.Name;
            stockDto.Value = EconomicDescription.close; 
            return Ok(stockDto);


        }

        //from our database ticker that same to the input string 
        //GET: /api/Stock/s/APPL
        [HttpGet("s+dayprice/{ticker}")]
        public async Task<ActionResult<Stock>> GetStockDailyByTicker(string ticker)
        {

            //var stock = await _readDataBase.GetStockByTickerAsync(ticker);
            //if (stock == null) { return NotFound(); }
            //var con = new JsonConverotr();
            //var stockPrice = await TiingoService.GetStockPrices(ticker, 1);
            //var TiingoPriceDtos = new List<TiingoPriceDto>(con.GetStockObjFromJson(stockPrice));
            //stock.Value = TiingoPriceDtos.FirstOrDefault().close;

            Stock s = await _readDataBase.GetStockByTickerAsync(ticker);
            if (s==null )
            {
                return NotFound();
            }
            var stockPrice = await TiingoService.GetStockPrices(ticker,5);
            var con = new JsonConverotr();
            var EconomicDescription = new List<TiingoPriceDto>(con.GetStockObjFromJson(stockPrice)).Last();
           
            s.TiingoPriceDtos.Add (EconomicDescription);
            s.Value = EconomicDescription.close;

            return Ok(s);
        }

        //our database full ticker or part of the name 
        //GET: /api/Stock/s/APPL
        [HttpGet("s/{input}")]
        public async Task<ActionResult<Stock>> GetStockNameSymbol(string input)
        {
            if (_dbContext.Stocks == null) { return NotFound(); }
            var stock = await _readDataBase.GetStockByTiingoStringAsync(input);
            if (stock == null) { return NotFound(); }
            return Ok(stock);
        }

        //our database list of the stocks that part of the name or ticker 
        //GET: /api/Stock/q/APPL
        [HttpGet("q/{query}")]
        public async Task<ActionResult<IEnumerable<Stock>>> GetStockByQuery(string query)
        {
            if (_dbContext.Stocks == null) { return NotFound(); }

            var stocks = await _readDataBase.GetStockByQueryList(query);

            if (stocks ==null) { return NotFound(); }

            return Ok(stocks);
        }

        //our database list one stock that part of the name or ticker 
        //GET: /api/Stock/q/APPL
        [HttpGet("StockDescription/{query}")]
        public async Task<ActionResult<string>> GetOneStockDescription(string query)
        {
            //if (_dbContext.Stocks == null) { return NotFound(); }

            var stock = await _readDataBase.GetOnerStockByQuery(query);
            if (stock == null) { return NotFound(); }
            return stock.Description;
        }



        //GET: /api/Stock/q/APPL/30
        [HttpGet("TiingoPriceDtoList/{ticker}/db/{days}")]
        public async Task<ActionResult<IEnumerable<TiingoPriceDto>>> GetTiingPriceList(string ticker, int days)
        {
            var stockPrice = await TiingoService.GetStockPrices(ticker, days);

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





        //PUT:
        [HttpPut("{id}")]
        public async Task<IActionResult> PutStock(int id, Stock stock)
        {
            if (id != stock.Id)
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
        public async Task<IActionResult> DeleteStock(int id)
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
            return stock;
        }
    }
}