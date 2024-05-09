using WSE_REST_WebApi.Models;
namespace WSE_REST_WebApi.DAL.Interfaces
{
    public interface InterfaceWriteToDatabase
    {

        //Stocks
        Task<Stock> AddMStockAsync(Stock stock);
        Task<Stock> UpdateStockAsync(Stock stock);
        Task DeleteStockAsync(Stock stock);


        //TiingoPriceDto
        //לבדוק מה בדיוק לעשות כאן מבחינת הקוד והיצירה האם צריך גם את המניה

        Task<TiingoPriceDto> AddTiingoPriceDtoAsync(Stock stock, TiingoPriceDto tiingoPriceDto);
        Task<TiingoPriceDto> UpdateTiingoPriceDtoAsync(Stock stock, TiingoPriceDto tiingoPriceDto);
        Task DeleteTiingoPriceDto(TiingoPriceDto tiingoPriceDto);


    }
}
