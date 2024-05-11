using Microsoft.AspNetCore.Mvc;
using WSE_REST_WebApi.Models;

namespace WSE_REST_WebApi.DAL.Interfaces
{
    public interface InterfaceReadFromDataBase
    {
      
        //Stocks
        Task<IEnumerable<Stock>> GetStocksAsync();
        Task<Stock?> GetStockByTiingoStringAsync(string ticker);
        Task<Stock?> GetStockByTickerAsync(string input);
        Task<IEnumerable<Stock>> GetStockByQueryList(string query);
        Task<Stock> GetOnerStockByQuery(string query);

        Task<Stock?> GetStockByIdAsync(int id);


        //TiingoPriceDTO
        Task<List<TiingoPriceDto?>> GetPricesByTiingoTickerAsync(string ticker);
        Task<List<TiingoPriceDto?>> GetPricesByIdAsync(int id);

    }
}
