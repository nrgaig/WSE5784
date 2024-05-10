using Newtonsoft.Json;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using WSE_REST_WebApi.Models;

namespace WSE_REST_WebApi.Models
{
    public class Stock
    {
        public int Id { get; set; }

        public string? Name { get; set; }

        public string? Ticker { get; set; }

        public string? Description { get; set; }


        // Navigation property
        public ICollection<TiingoPriceDto> TiingoPriceDtos { get; set; } = new List<TiingoPriceDto>();

        public double? Value { get; set; }
        //public double? Open { get; set; }



    }

}


//[NotMapped]
//[JsonIgnore]
//public List<TiingoPriceDto>? EconomicDescription { get; set; }

