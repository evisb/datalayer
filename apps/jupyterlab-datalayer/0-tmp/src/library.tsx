import * as React from 'react';
import { Provider } from 'react-redux'
import { ConnectedRouter } from 'react-router-redux'
import routerHistory from '@datalayer/datalayer/lib/history/History'
import { DatalayerStore } from '@datalayer/datalayer/lib/store/DatalayerStore'
import SparkStatus from '@datalayer/datalayer/lib/spark/SparkStatus'

export interface IProps {
}

export interface IState {
}

// JupyterLab Extension for Kubernetes Authentication and Authorization in the Cloud (AWS...).
export class Library extends React.Component<IProps, IState> {

  public constructor(props: IProps) {
    super(props)
  }

  public render() {
    return (
      <div style={{
        position: 'relative',
        width: '100%',
        padding: '10px'
        }}>
        <div className="ms-slideDownIn20" style={{ height: "100vh" }}>
          <div className="ms-font-su">Library</div>
          <img src="https://datalayer.io/images/datalayer/library-artifacts.svg"/>
        </div>
        <Provider store={ DatalayerStore.notebookStore }>
          <div>
            <ConnectedRouter history = { routerHistory } >
              <SparkStatus />
            </ConnectedRouter>
          </div>
        </Provider>
      </div>
    );
  }

}
