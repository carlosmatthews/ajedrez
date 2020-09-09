import React, { Component } from 'react';

class Tablero extends Component {
  render() {
    const props = this.props;
    const tablero = props.tablero;
    if (tablero === null) return <p>Tablero no cargado...</p>;
    const rango_8 = [];
    for (let i = 0; i < 8; i++) {rango_8.push(i);}

    const filas = []
    for (const f of rango_8) {
      const fila = [];
      for (const c of rango_8) {
        fila.push(tablero[[f,c]]);
      }
      filas.push(fila);
    }
    filas.reverse();
    return <div id="container_tablero">
      <table id="tablero">
        <tbody>
          {filas.map((fila, f) =>
            <FilaTablero key={f}
                         f={7-f}
                         fila={fila}
                         click={props.click}
                         mov_posibles={props.mov_posibles}
                         pos_seleccionada={props.pos_seleccionada}/>
          )}
          <tr>
          <td></td>
          {rango_8.map(i => <td key={i}>{String.fromCharCode('a'.charCodeAt(0) + i)}</td>)}
          </tr>
        </tbody>
      </table>
    </div>;
  }
}

export const representacion_pieza = function(pieza) {
  const piezas = {};
  piezas[['R','B']] = '♔';
  piezas[['RA','B']] = '♕';
  piezas[['T','B']] = '♖';
  piezas[['C','B']] = '♘';
  piezas[['A','B']] = '♗';
  piezas[['P','B']] = '♙';
  piezas[['R','N']] = '♚';
  piezas[['RA','N']] = '♛';
  piezas[['T','N']] = '♜';
  piezas[['C','N']] = '♞';
  piezas[['A','N']] = '♝';
  piezas[['P','N']] = '♟︎';
  return piezas[pieza];
};

const FilaTablero = (props) => <tr>
  <td>{props.f + 1}</td>
  { props.fila.map((casillero, c) =>
    <Casillero key={[props.f, c]}
               f={props.f}
               c={c}
               casillero={casillero}
               mov_posibles={props.mov_posibles}
               pos_seleccionada={props.pos_seleccionada}
               click={props.click}/>
   )}
</tr>;

class Casillero extends Component {
  render() {
    const props = this.props;
    const f = props.f;
    const c = props.c;
    const casillero = props.casillero;
    const pos_seleccionada = props.pos_seleccionada;
    const pieza = representacion_pieza(casillero);

    const color = (f + c) % 2 === 0 ? 'oscuro' : 'claro';
    const es_posible = props.mov_posibles.findIndex(([e0,e1]) => e0 === f && e1 === c) >= 0;
    const es_seleccionada = pos_seleccionada && pos_seleccionada[0] === f && pos_seleccionada[1] === c;
    const classes = `casillero ${color} ${es_posible && 'posible'} ${es_seleccionada && 'seleccionada'}`;
    return <td className={classes} onClick={()=>props.click(f, c)}>{pieza}</td>;
  }
}

export default Tablero;
