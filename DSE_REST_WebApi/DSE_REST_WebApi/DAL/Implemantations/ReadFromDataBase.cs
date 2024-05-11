using WSE_REST_WebApi.DAL.Interfaces;
using Microsoft.EntityFrameworkCore;
using WSE_REST_WebApi.Models;
using WSE_REST_WebApi.DAL;
using WSE_REST_WebApi.Models;
using Microsoft.AspNetCore.Mvc;

namespace WSE_REST_WebApi.DAL.Implemantations
{
    public class ReadFromDataBase : InterfaceReadFromDataBase
    {
        private readonly StockContext _dbContext;

        public ReadFromDataBase(StockContext dbContext)
        {
            _dbContext = dbContext;
        }


        //Stocks
        public async Task<IEnumerable<Stock>> GetStocksAsync()
        {
            var stocks = await _dbContext.Stocks.ToListAsync();
            return stocks;
        }

        public async Task<Stock?> GetStockByTiingoStringAsync(string input)
        {
            var stock = await _dbContext.Stocks.FirstOrDefaultAsync(s => s.Ticker == input || s.Name.Contains(input ));
            return stock;
        }

        public async Task<Stock?> GetStockByIdAsync(int stockId)
        {
            var stock = await _dbContext.Stocks.FindAsync(stockId);
            return stock;
        }

        public async Task<Stock?> GetStockByTickerAsync(string ticker)
        {
            var stock = await _dbContext.Stocks.FirstOrDefaultAsync(s => s.Ticker == ticker);
            return stock;
        }

        public async Task<IEnumerable<Stock>> GetStockByQueryList(string query)
        {
            var stocks = await _dbContext.Stocks
                .Where(s => s.Name.Contains(query) || s.Ticker.Contains(query))
                .ToListAsync();
            return stocks;

        }

        public async Task<Stock> GetOnerStockByQuery(string query)
        {
            var stock = await _dbContext.Stocks
                .Where(s => s.Name.Contains(query) || s.Ticker.Contains(query))
                .FirstOrDefaultAsync();
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