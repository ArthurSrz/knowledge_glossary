# Spatial Reference System Identifier (SRID)

## Definition

A Spatial Reference System Identifier (SRID) is a unique numerical code that identifies specific coordinate reference systems used to define locations on Earth, originated by the European Petroleum Survey Group (EPSG) in 1985 as a standardized registry for geodetic parameters.

## Historical Development

1. **EPSG Formation (1985)**: European Petroleum Survey Group established
2. **EPSG Registry Creation**: First standardized database of spatial references
3. **ISO 19111 Standard (2003)**: International standardization
4. **OGC Standards (2000s)**: Open Geospatial Consortium adoption
5. **Modern Management (2005+)**: International Association of Oil & Gas Producers (IOGP)

## EPSG's Original Concept

The EPSG established:
- Unique numerical identifiers for coordinate systems
- Standardized geodetic parameter definitions
- Registry of Earth ellipsoids and datums
- Coordinate transformation parameters
- Units of measurement standards

## Key Components

1. **Geodetic Datum**:
   - Reference ellipsoid
   - Origin point
   - Orientation parameters
   - Datum shifts

2. **Coordinate System Type**:
   - Geographic (latitude/longitude)
   - Projected (planar coordinates)
   - Vertical (elevation references)
   - Compound (combination systems)

3. **Projection Parameters**:
   - Projection method
   - Central meridian
   - Scale factor
   - False easting/northing

## Common SRID Examples

1. **EPSG:4326**: WGS 84 (GPS standard)
2. **EPSG:3857**: Web Mercator (Google Maps)
3. **EPSG:32633**: UTM Zone 33N
4. **EPSG:2154**: RGF93 / Lambert-93 (France)
5. **EPSG:27700**: OSGB 1936 (British National Grid)

## Technical Structure

1. **Registry Format**:
   - Unique integer identifier
   - Authority (usually EPSG)
   - Version control
   - Metadata fields

2. **Database Schema**:
   - Coordinate reference systems
   - Coordinate operations
   - Datum definitions
   - Units and parameters

3. **Implementation**:
   - SQL spatial databases
   - GIS software
   - Mapping libraries
   - Web services

## Applications

1. **Geographic Information Systems**:
   - Data integration
   - Coordinate transformation
   - Map projection
   - Spatial analysis

2. **Surveying and Mapping**:
   - Land surveying
   - Cartography
   - Navigation
   - Engineering projects

3. **Location-Based Services**:
   - GPS applications
   - Mobile mapping
   - Asset tracking
   - Geolocation services

4. **Scientific Research**:
   - Earth sciences
   - Climate studies
   - Environmental monitoring
   - Resource exploration

## Standards and Protocols

1. **ISO 19111**: Geographic information - Spatial referencing
2. **OGC Standards**: Well-Known Text (WKT), GML
3. **PROJ Library**: Coordinate transformation software
4. **Spatial SQL**: PostGIS, Oracle Spatial, SQL Server

## Impact on Industry

1. **Petroleum Industry**: Original driver for standardization
2. **GIS Development**: Foundation for interoperability
3. **Web Mapping**: Enabled consistent global services
4. **Data Exchange**: Facilitated international collaboration

## Best Practices

1. **Metadata Management**:
   - Always specify SRID
   - Document transformations
   - Maintain version history

2. **Accuracy Considerations**:
   - Choose appropriate SRID
   - Consider precision requirements
   - Account for datum shifts

3. **Performance Optimization**:
   - Use appropriate projections
   - Minimize transformations
   - Cache commonly used systems

## Common Challenges

1. **Datum Transformations**: Accuracy limitations
2. **Legacy Systems**: Outdated SRID definitions
3. **Regional Variations**: Local coordinate systems
4. **Vertical References**: Elevation system complexities

## Modern Developments

1. **Dynamic Datums**: Time-dependent references
2. **3D/4D Coordinates**: Including time dimension
3. **Web Standards**: GeoJSON, WFS, WMS
4. **Open Source Tools**: GDAL, PROJ, PostGIS

## Related Concepts
- [[Coordinate reference system]]
- [[Geodetic datum]]
- [[Map projection]]
- [[Geographic information system]]
- [[Spatial database]]

## References

European Petroleum Survey Group. (1985). EPSG Geodetic Parameter Dataset. 

ISO 19111:2019. Geographic information — Referencing by coordinates.