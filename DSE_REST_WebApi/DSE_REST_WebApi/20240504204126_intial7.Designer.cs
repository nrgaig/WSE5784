﻿// <auto-generated />
using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.EntityFrameworkCore.Migrations;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using WSE_REST_WebApi.Models;

#nullable disable

namespace WSE_REST_WebApi.Migrations
{
    [DbContext(typeof(StockContext))]
    [Migration("20240504204126_intial7")]
    partial class intial7
    {
        protected override void BuildTargetModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "6.0.28")
                .HasAnnotation("Relational:MaxIdentifierLength", 128);

            SqlServerModelBuilderExtensions.UseIdentityColumns(modelBuilder, 1L, 1);

            modelBuilder.Entity("WSE_REST_WebApi.Models.Stock", b =>
                {
                    b.Property<int>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("int");

                    SqlServerPropertyBuilderExtensions.UseIdentityColumn(b.Property<int>("Id"), 1L, 1);

                    b.Property<string>("Description")
                        .HasColumnType("nvarchar(max)");

                    b.Property<string>("Name")
                        .HasColumnType("nvarchar(max)");

                    b.Property<string>("Ticker")
                        .HasColumnType("nvarchar(max)");

                    b.Property<double?>("Value")
                        .HasColumnType("float");

                    b.HasKey("Id");

                    b.ToTable("Stocks");
                });

            modelBuilder.Entity("WSE_REST_WebApi.Models.TiingoPriceDto", b =>
                {
                    b.Property<int>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("int");

                    SqlServerPropertyBuilderExtensions.UseIdentityColumn(b.Property<int>("Id"), 1L, 1);

                    b.Property<int>("StockId")
                        .HasColumnType("int");

                    b.Property<double?>("close")
                        .HasColumnType("float");

                    b.Property<string>("date")
                        .HasColumnType("nvarchar(max)");

                    b.Property<double?>("divCash")
                        .HasColumnType("float");

                    b.Property<double?>("high")
                        .HasColumnType("float");

                    b.Property<double?>("low")
                        .HasColumnType("float");

                    b.Property<double?>("open")
                        .HasColumnType("float");

                    b.Property<double?>("splitFactor")
                        .HasColumnType("float");

                    b.Property<double?>("volume")
                        .HasColumnType("float");

                    b.HasKey("Id");

                    b.HasIndex("StockId");

                    b.ToTable("TiingoPriceDtos");
                });

            modelBuilder.Entity("WSE_REST_WebApi.Models.TiingoPriceDto", b =>
                {
                    b.HasOne("WSE_REST_WebApi.Models.Stock", "Stock")
                        .WithMany("TiingoPriceDtos")
                        .HasForeignKey("StockId")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation("Stock");
                });

            modelBuilder.Entity("WSE_REST_WebApi.Models.Stock", b =>
                {
                    b.Navigation("TiingoPriceDtos");
                });
#pragma warning restore 612, 618
        }
    }
}
