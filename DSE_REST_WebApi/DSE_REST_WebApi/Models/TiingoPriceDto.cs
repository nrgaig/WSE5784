using Newtonsoft.Json;

namespace WSE_REST_WebApi.Models
{
    public class TiingoPriceDto
    {
        public int Id { get; set; }
        public string? date { get; set; }
        public double? close { get; set; }
        public double? high { get; set; }
        public double? low { get; set; }
        public double? open { get; set; }
        public double? volume { get; set; }
        public double? divCash { get; set; }
        public double? splitFactor { get; set; }

        // Foreign key
        public int StockId { get; set; }

        // Navigation property
        [JsonIgnore]
        public Stock Stock { get; set; } = null!;
    }
}
