import * as React from 'react';
import ReduxToastr from 'react-redux-toastr'
import { Provider } from 'react-redux'
import { ConnectedRouter } from 'react-router-redux'
import routerHistory from '@datalayer/datalayer/lib/history/History'
import { DatalayerStore } from '@datalayer/datalayer/lib/store/DatalayerStore'
import ConfigApi from '@datalayer/datalayer/lib/api/config/ConfigApi'
import GoogleApi from '@datalayer/datalayer/lib/api/google/GoogleApi'
import MicrosoftApi from '@datalayer/datalayer/lib/api/microsoft/MicrosoftApi'
import TwitterApi from '@datalayer/datalayer/lib/api/twitter/TwitterApi'
import SpitfireApi from '@datalayer/datalayer/lib/api/spitfire/SpitfireApi'
import DatalayerApi from '@datalayer/datalayer/lib/api/datalayer/DatalayerApi'

export interface IProps {
}

export interface IState {
}

// JupyterLab Extension for Kubernetes Authentication and Authorization in the Cloud (AWS...).
export class Init extends React.Component<IProps, IState> {

  public constructor(props: IProps) {
    super(props)
  }

  public render() {
    return (
        <Provider store={ DatalayerStore.notebookStore }>
          <div>
            <ConfigApi/>
            <SpitfireApi/>
            <DatalayerApi/>
            <GoogleApi/>
            <MicrosoftApi/>
            <TwitterApi/>
            <ConnectedRouter history = { routerHistory } >
            </ConnectedRouter>
            <ReduxToastr
              timeOut={4000}
              newestOnTop={false}
              preventDuplicates={true}
              position="top-right"
              transitionIn="fadeIn"
              transitionOut="fadeOut"
              progressBar={true}
            />
          </div>
        </Provider>
    );
  }

}
