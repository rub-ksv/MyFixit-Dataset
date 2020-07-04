# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A simple script for extracting the relevant documents and saving in xml or json format

import argparse
import json
import os
import itertools

if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(
        description='Querying Myfixit dataset according to the arguments and writing the result in desired format'
        ,
        usage='querymyfixit -device device_name -category category_of_device -part part_to_repair '
              '-minsteps minimum_nomber_of_steps -mintools minimum_number_of_tools -outformat output_format (xml|json) '
              '-out output_file -verbose -annotatedpart -annotatedtool')

    parser.add_argument('-device', nargs='+', help="Name of the device")
    parser.add_argument('-input', help="Input file")
    parser.add_argument('-part',  nargs='+', help="Part of device to repair")
    parser.add_argument('-format', help="The format of output data , xml or json")
    parser.add_argument('-output', help="Path to the output file")
    parser.add_argument('-mintools', help="Minimum number of tools", type=int)
    parser.add_argument('-minsteps', help="Minimum number of steps", type=int)
    parser.add_argument('-annotatedtool', help="Only seleting the manuals with the annotation of reqired tool", action="store_true")
    parser.add_argument('-annotatedpart', help="Only seleting the manuals with the annotation of disassembled parts", action="store_true")
    parser.add_argument("-verbose", help="Print the title of selected manuals",
                        action="store_true")

    args = parser.parse_args()

    if args.input:
        input = args.input
        pth = os.path.join('jsons/', input)
        if not os.path.exists(pth):
            print('The existing files are {}'.format(os.listdir('jsons')))
            raise AssertionError('The selected json file does not exist.')
    else:
        raise AssertionError('Please select a input file')

    if args.device:
        device = ' '.join([i.lower() for i in args.device]).strip()
    else:
        device = None

    if args.mintools:
        mintools = args.mintools
    else:
        mintools = None

    if args.minsteps:
        minsteps = args.minsteps
    else:
        minsteps = None

    if args.part:
        part = ' '.join([i.lower() for i in args.part]).strip()
    else:
        part = None

    if args.output:
        output = args.output
    else:
        raise AssertionError('Please enter the output file')

    out_format = 'json'
    if args.format:
        if args.format.lower() == 'json' or args.format.lower() == 'xml':
            out_format = args.format.lower()
        else:
            raise AssertionError('Only support xml and json for output format')

    jlist = []
    with open(pth, 'r') as f:
        for line in f:
            _tmpdict = (json.loads(line))
            _tmpdict_keys = itertools.chain.from_iterable([i.keys() for i in _tmpdict['Steps']])
            if device and device not in [i.lower() for i in _tmpdict['Ancestors']]:
                continue
            if part and part not in [i.lower() for i in _tmpdict['Title'].split()]:
                continue
            if mintools and mintools > len(_tmpdict['Toolbox']):
                continue
            if minsteps and minsteps > len(_tmpdict['Steps']):
                continue
            if args.annotatedtool and 'Tools' not in _tmpdict_keys:
                continue
            if args.annotatedpart and 'Word_level_parts_raw' not in _tmpdict_keys:
                continue
            jlist.append(_tmpdict)

    print('Total number of matched manuals :{}'.format(len(jlist)))

    if args.verbose:
        print('Title of manuals:')
        for i in jlist:
            print(i['Title'])

    if out_format == 'json':
        with open(output + '.json', 'w+') as f:
            json.dump(jlist, f)

        print('Selected manuals are saved in {}'.format(output + '.json'))

    else:
        from dicttoxml import dicttoxml
        with open(output + '.xml', 'w+') as f:
            f.write(str(dicttoxml(jlist, attr_type=False).decode()))

        print('Selected manuals are saved in {}'.format(output + '.xml'))
