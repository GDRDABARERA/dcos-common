#!/usr/bin/python
# ------------------------------------------------------------------------
#
# Copyright 2016 WSO2, Inc. (http://wso2.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License

# ------------------------------------------------------------------------
import sys, json;

def main():
    data = json.load(sys.stdin)
    if (data is None or 'tasks' not in data):
        print "Error! Marathon application for marathon-lb is not found"
        sys.exit(1)

    if (len(data['tasks']) == 0):
        print "Error! No tasks found for marathon-lb"
        sys.exit(1)

    if ('host' not in data['tasks'][0]):
        print "Host is not found for marathon-lb task"
        sys.exit(1)

    print data['tasks'][0]['host']
    sys.exit(0)

if __name__ == "__main__":
    main()
