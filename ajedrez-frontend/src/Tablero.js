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
    this.setState({tablero: {} }); // TODO: llamar API de carli
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
        fila.push(null);
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
  { props.fila.map((columna, c) =>
    <Casillero key={[props.f, c]}
               f={props.f}
               c={c}
               mov_posibles={props.mov_posibles}
               click={props.click}/>
   )}
</tr>;

class Casillero extends Component {
  render() {
    const props = this.props;
    const f = props.f;
    const c = props.c;
    const color = (f + c) % 2 === 0 ? 'claro' : 'oscuro';
    const es_posible = props.mov_posibles.findIndex(([e0,e1]) => e0 === f && e1 === c) >= 0;
    return <td className={`${color} ${es_posible && 'posible'}`} onClick={()=>props.click(f, c)}></td>;
  }
}

export default Tablero;
