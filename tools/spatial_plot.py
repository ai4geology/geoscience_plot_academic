import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def spatial_points_plot(csv_path, size, DPI, LandA,out_path, type):
    df = pd.read_csv(csv_path)

    fig = plt.figure(figsize=size,dpi=DPI)
    ax = plt.figure(projection=ccrs.PlateCarree())
    ax.set_extent(LandA, crs=ccrs.PlateCarree())
    ax.stock_img()

    plt.scatter(data=df, x='Long', y='Lat', s=0.5, c='SiO2', vmin=45, vmax=80, cmap="cool",alpha=1,transform=ccrs.PlateCarree())
    plt.colorbar(extend='both', label='SiO2 (wt%)', pad=0.15, shrink=0.85)

    ax.gridlines(draw_labels=True)  # 显示经纬网格
    plt.savefig(out_path + type dpi=DPI, bbox_inches='tight', pad_inches=0.2)
    plt.show()

def heat_plot(csv_path, size, DPI,LandA,out_path, type):
    df = pd.read_csv(csv_path)

    fig = plt.figure(figsize=size, dpi=DPI)
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent(LandA, crs=ccrs.PlateCarree())


    ax.add_feature(cfeature.LAND, facecolor='lightgray')
    ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
    ax.add_feature(cfeature.RIVERS, edgecolor='blue', linewidth=0.5)

    sns.kdeplot(
        data=df,
        x="Long",
        y="Lat",
        cmap="Reds",
        shade=True,
        cbar=True,
        cbar_kws=dict(shrink=0.6),
        transform=ccrs.PlateCarree(),
        n_levels=100,  # increase the level to smooth the color increments, default n_level=10
        ax=ax,
    )

    # Set the font size of the labels
    gl = ax.gridlines(draw_labels=True)
    gl.xlabel_style = {'size': 5}
    gl.ylabel_style = {'size': 5}
    plt.savefig(out_path + type, dpi=DPI, bbox_inches='tight', pad_inches=0.2)
    plt.show()