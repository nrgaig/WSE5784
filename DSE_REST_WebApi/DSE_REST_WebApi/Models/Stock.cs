using System.ComponentModel.DataAnnotations.Schema;

namespace WSE_REST_WebApi.Models
{
    public class Stock
    {
        public int Id { get; set; }

        public string? Name { get; set; }

        public string? Ticker { get; set; }

        public string? Description { get; set; }

        [NotMapped]
        public List<TiingoPriceDto>? EconomicDescription { get; set; }
    }

}

