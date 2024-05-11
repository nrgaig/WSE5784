using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace WSE_REST_WebApi.Migrations
{
    public partial class initial10 : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "Open",
                table: "Stocks");
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<double>(
                name: "Open",
                table: "Stocks",
                type: "float",
                nullable: true);
        }
    }
}
