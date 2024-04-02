using Microsoft.EntityFrameworkCore;

namespace WSE_REST_WebApi.Models
{
    public class StockContext:DbContext
    {
       public StockContext(DbContextOptions<StockContext> options) : base(options) { }
       public  DbSet<Stock> Stocks { get; set; } = null!;
    }


}
