# deployment script for all datapipes

import boto3.session
import json
import os

def deploy():

    session = boto3.session.Session(profile_name='personal')

    iam_result = deploy_iam_roles(session)


def deploy_iam_roles(session):

    # get list of roles in iam dir
    iam_role_files = os.listdir(role_dir)

    # create session
    iam_client = session.client('iam')

    for role_file in os.listdir('iam/roles'):

        role_name, _ = os.path.splitext(role_file)

        # load in role and policy configs
        role = json.load(open('/'.join((role_dir, role_file))))
        policy = json.load(open('iam/policies/{}.json'.format(role['policy'])))

        print 'creating role: {}'.format(role_name)
        try:
            iam_client.create_role(
                    RoleName=role_name,
                    AssumeRolePolicyDocument=json.dumps(policy))
        except:
            print 'role already exists'



if __name__ == '__main__':
    deploy()
