using WSE_REST_WebApi.DAL.Interfaces;
using Microsoft.EntityFrameworkCore;
using WSE_REST_WebApi.Models;
using WSE_REST_WebApi.DAL;
using  WSE_REST_WebApi.Models;

namespace WSE_REST_WebApi.DAL.Implemantations
{
    public class ReadFromDataBase: InterfaceReadFromDataBase
    {
        private readonly StockContext _dbContext;

        public ReadFromDataBase(StockContext dbContext)
        {
            _dbContext = dbContext;
        }


        //Stocks
        public async Task<IEnumerable<Stock>> GetStocksAsync()
        {
            var stocks= await _dbContext.Stocks.ToListAsync();
            return stocks;
        }

        public async Task<Stock?> GetStockByTiingoStringAsync(string input)
        {
            var stock = await _dbContext.Stocks.FirstOrDefaultAsync(s => s.Name == input || s.Ticker == input);
            return stock;
        }

        public async Task<Stock?> GetStockByIdAsync(int stockId)
        {
            var stock = await _dbContext.Stocks.FindAsync(stockId);
            return stock;
        }


        //TiingoPriceDTO
       public async Task<List<TiingoPriceDto?>> GetPricesByTiingoTickerAsync(string ticker)
        {
            var stock = GetStockByTiingoStringAsync(ticker);
            int stockId = stock.Id;
            return await GetPricesByIdAsync(stockId);
            
            
        }
       public async Task<List<TiingoPriceDto?>> GetPricesByIdAsync(int id)
        {
            return await _dbContext.GetTiingoPricesFromStockId(id);
        }
    }
}
