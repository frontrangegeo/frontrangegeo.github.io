<p style="vertical-align: middle; width: 100%;">
<img src="resources/FRGLogo.png" style="float: left; max-height: 5em;"/>
<h1>Phoenix Refraction Statics</h1>
</p>

<img src="resources/geopcombined.png" style="width: 65%; float: left; padding-right: 10px;"/>
<p style="padding-left: 50px;">Phoenix is a near surface modeling and refraction statics package designed for the next generation of seismic surveys. Designed to run the largest datasets in hours instead of weeks, Phoenix offers unheard-of&nbsp;performance.<br></br>With vastly superior geophysical modeling capabilities, integration of additional well-log data as constraints, and seamless survey merges, Phoenix offers seismic processing options that can't be found anywhere else.<br></br>
*Left: Velocity inversion found using Phoenix ANS tomography.*
</p>

<h2 style="padding-top: 5px;">Speed</h2>
<img src="resources/PhxFlatTimesTransparent.png" style="width: 65%; float: right;"/>
Every day tasks such as data import and survey merges, delay time and tomographic modeling, picking and QC procedures have all been parallelized and distributed, leading to speedup factors of **10-100x** over competitive software such as Flatirons.

*Right: 400M trace survey, running on 3 node cluster. Phoenix speed advantage scales with compute resources.*

## Quality
Phoenix introduces a brand new tomographic inversion algorithm, Adaptive Node Spacing (ANS), that dynamically adjusts grid resolution to maximize detail in areas where it is needed, and save computation in areas where it is not.

<div style="-webkit-column-count: 2; -moz-column-count: 2; column-count: 2; -webkit-column-rule: 1px dotted #e0e0e0; -moz-column-rule: 1px dotted #e0e0e0; column-rule: 1px dotted #e0e0e0;">

<div style="display: inline-block;">


![](resources/combinedANS.png)
*ANS Tomo slice from Teapot Dome survey<br> Note improved refractor boundary delineation*
</div>

<p></p>


<div style="display: inline-block;">

![](resources/combinedVNS.png)
*VNS Tomo slice from Teapot Dome survey*

</div>
</div>

## Picking
Phoenix integrates directly with Front Range's AI for first break picking, DeepTrace. Automatically pick your largest and noisiest surveys in hours automatically, instead of weeks of manual labor.
<div style="-webkit-column-count: 2; -moz-column-count: 2; column-count: 2; -webkit-column-rule: 1px dotted #e0e0e0; -moz-column-rule: 1px dotted #e0e0e0; column-rule: 1px dotted #e0e0e0;">

<div style="display: inline-block;">


![](resources/lefthalfdeeptrace.png)
*Automatic picking with DeepTrace*
</div>

<p></p>


<div style="display: inline-block;">

![](resources/lefthalfauto.png)
*Traditional threshhold autopicker*

</div>
</div>