-- SQLite
-- 1. Primeros 10 viajes registrados pagados con boleto físico
Select *
from afluencia_rtp
where tipo_pago = 'Boleto'
limit 10;

-- 2. Días y servicios con afluencia récord (mayor a 100,000 pasajeros)
Select *
from afluencia_rtp
where afluencia > 100000
order by afluencia desc
limit 10;

-- 3. Afluencia desglosada por tipo de pago para una fecha específica
Select *
from afluencia_rtp
where fecha = '2025-03-14'
order by tipo_pago, afluencia desc
limit 15;