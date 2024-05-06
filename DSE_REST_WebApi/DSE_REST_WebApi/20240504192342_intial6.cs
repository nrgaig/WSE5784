using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace WSE_REST_WebApi.Migrations
{
    public partial class intial6 : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "TiingoPriceDtos",
                columns: table => new
                {
                    Id = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    date = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    close = table.Column<double>(type: "float", nullable: true),
                    high = table.Column<double>(type: "float", nullable: true),
                    low = table.Column<double>(type: "float", nullable: true),
                    open = table.Column<double>(type: "float", nullable: true),
                    volume = table.Column<double>(type: "float", nullable: true),
                    divCash = table.Column<double>(type: "float", nullable: true),
                    splitFactor = table.Column<double>(type: "float", nullable: true),
                    StockId = table.Column<int>(type: "int", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_TiingoPriceDtos", x => x.Id);
                    table.ForeignKey(
                        name: "FK_TiingoPriceDtos_Stocks_StockId",
                        column: x => x.StockId,
                        principalTable: "Stocks",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateIndex(
                name: "IX_TiingoPriceDtos_StockId",
                table: "TiingoPriceDtos",
                column: "StockId");
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "TiingoPriceDtos");
        }
    }
}
