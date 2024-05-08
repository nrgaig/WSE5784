using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;

namespace WSE_REST_WebApi.Models
{
    public class StockContext:DbContext
    {
       public StockContext(DbContextOptions<StockContext> options) : base(options) { }
       public  DbSet<Stock> Stocks { get; set; } = null!;
       public DbSet<TiingoPriceDto> TiingoPriceDtos { get; set; } = null!;
       public async Task<List<TiingoPriceDto>> GetTiingoPricesFromStockId(int stockId)
        {
            List<TiingoPriceDto> prices = await TiingoPriceDtos.Where(t => t.StockId == stockId).ToListAsync();
            return prices;
            //return TiingoPriceDtos.Where(t => t.StockId == stockId).ToList();
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<TiingoPriceDto>()
                .HasOne(tp => tp.Stock)
                .WithMany(s => s.TiingoPriceDtos)
                .HasForeignKey(tp => tp.StockId);
        }
        //public DbSet<TiingoPriceDto> TiingoPrices { get; set; }

        //protected override void OnModelCreating(ModelBuilder modelBuilder)
        //{
        //    modelBuilder.Entity<TiingoPriceDto>().HasNoKey();
        //}
    }


}
