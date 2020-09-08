import React, { Component } from 'react';

class Tablero extends Component {
  constructor(props) {
    super(props);
    this.state = {
      tablero: null,
      mov_posibles: [],
    }
  }

  componentDidMount() {this.cargar_tablero();}

  cargar_tablero() {
    console.log('cargar tablero');
    const tablero = {}; // TODO: llamar API de carli
    tablero[[1,0]] = ['P', 'B'];
    tablero[[1,1]] = ['P', 'B'];
    tablero[[0,0]] = ['T', 'B'];
    tablero[[0,1]] = ['C', 'B'];
    tablero[[0,2]] = ['A', 'B'];
    tablero[[0,3]] = ['RA', 'B'];
    tablero[[0,4]] = ['R', 'N'];

    tablero[[6,7]] = ['P', 'N'];
    tablero[[7,0]] = ['T', 'N'];
    tablero[[7,1]] = ['C', 'N'];
    tablero[[7,2]] = ['A', 'N'];
    tablero[[7,3]] = ['RA', 'N'];
    tablero[[7,4]] = ['R', 'N'];
    this.setState({tablero: tablero});
  }

  click_casillero(f,c) {
    console.log('hola', f, c);
  }

  render() {
    const state = this.state;
    const tablero = state.tablero;
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
      <h3>Tablero:</h3>
      <table id="tablero">
        <tbody>
          {filas.map((fila, f) => <FilaTablero key={f} f={7-f} fila={fila} click={this.click_casillero} mov_posibles={state.mov_posibles}/>)}
          <tr>
          <td></td>
          {rango_8.map(i => <td key={i}>{String.fromCharCode('a'.charCodeAt(0) + i)}</td>)}
          </tr>
        </tbody>
      </table>
    </div>;
  }
}

const FilaTablero = (props) => <tr>
  <td>{props.f + 1}</td>
  { props.fila.map((casillero, c) =>
    <Casillero key={[props.f, c]}
               f={props.f}
               c={c}
               casillero={casillero}
               mov_posibles={props.mov_posibles}
               click={props.click}/>
   )}
</tr>;

class Casillero extends Component {
  render() {

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

    const props = this.props;
    const f = props.f;
    const c = props.c;
    const casillero = props.casillero;
    const color = (f + c) % 2 === 0 ? 'oscuro' : 'claro';
    const es_posible = props.mov_posibles.findIndex(([e0,e1]) => e0 === f && e1 === c) >= 0;
    const pieza = casillero ? piezas[casillero] : '';
    console.log(f,c, pieza, pieza);
    return <td className={`casillero ${color} ${es_posible && 'posible'}`} onClick={()=>props.click(f, c)}>{pieza}</td>;
  }
}

export default Tablero;
